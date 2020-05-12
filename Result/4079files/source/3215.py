import redis as r

from datetime import datetime, timedelta

from .translation import localize_timedelta


def build_cache_key(**arguments) -> str:
    """
    Создаёт строковый ключ кэша из всех строк ключей и значений словаря

    >>> build_cache_key(arg1='value1', arg2='value2')
    'arg1;value1;arg2;value2'

    >>> build_cache_key(user=User('vasya man'), scope=Organization('Org1'))
    'scope;Организация:_Org1;user;vasya_man'
    """
    parts = []
    for k in sorted(arguments):
        parts.append(k)
        parts.append(arguments[k])
    return ';'.join(map(lambda s: str(s).replace(' ', '_'), parts))


class ThrottlingOptions:
    """
    Класс с набором настроек, которые будут использоваться корзинами.
    Можно изменять значения переменных как в самом классе, так и передавать экземпляр класса
    в конструктор ThrottlingBucket.

    periods_to_overtake - кол-во периодов, неиспользованную ёмкость которых пользователь
                          может наверстать путём совершения запросов.
    redis_instance      - StrictRedis instance. Если не задан, создаётся автоматически.
    redis_options       - словарь настроек для конструктора StrictRedis.
    verbose_mode        - писать отладочную информацию в print или нет
    """
    periods_to_overtake = 0
    redis_instance = None
    redis_options = {}
    verbose_mode = False

    def __init__(self, periods_to_overtake=0, redis_instance=None, redis_options=None, verbose_mode=False):
        self.periods_to_overtake = periods_to_overtake
        self.redis_instance = redis_instance
        self.redis_options = redis_options or {}
        self.verbose_mode = verbose_mode

    @property
    def redis(self):
        if not self.redis_instance:
            self.redis_instance = r.StrictRedis(**self.redis_options)
        return self.redis_instance


defaultThrottlingOptions = ThrottlingOptions()


class ThrottlingRule:
    """
    Класс с двумя переменными, характеризующими частоту запросов:
    1) кол-во запросов
    2) интервал времени
    """
    max_requests = None
    interval = None

    def __init__(self, max_requests: int, interval: [timedelta, int]):
        self.max_requests = max_requests
        if isinstance(interval, timedelta):
            self.interval = interval
        else:
            self.interval = timedelta(seconds=interval)

    def __str__(self):
        return 'ThrottlingRule: %d requests per %s' % (self.max_requests,
                                                       localize_timedelta(self.interval))

    @property
    def cache_key(self) -> str:
        return build_cache_key(requests=self.max_requests, per=self.interval)


class ThrottlingBucket:
    updated_at_key = 'updated_at'
    capacity_key = 'capacity'
    base_key = None
    cache_dict = None
    rule = None
    request = None
    options = None

    def __init__(self, rule: ThrottlingRule, arguments_bundle: dict, options: ThrottlingOptions=None):
        self.options = options or defaultThrottlingOptions
        self.base_key = 'THROTTLING:%s%s' % (rule.cache_key, build_cache_key(**arguments_bundle))
        self.rule = rule
        self.cache_dict = {k.decode(): v for (k, v) in self._redis.hgetall(self.base_key).items()}

    @property
    def _capacity(self) -> [None, int]:
        """Оставшаяся ёмкость ведра"""
        d = self.cache_dict.get(self.capacity_key)
        return int(d) if d is not None else d

    @property
    def _updated_at(self) -> [None, timedelta]:
        """Время обновления ведра"""
        d = self.cache_dict.get(self.updated_at_key)
        return datetime.fromtimestamp(float(d)) if d is not None else d

    @property
    def _redis(self):
        return self.options.redis

    def _log(self, *msg):
        if self.options.verbose_mode:
            print(*msg)

    def check_throttle(self) -> [None, timedelta]:
        """
        Возвращает None, если лимит ведра не превышен,
        иначе интервал времени, через который ведро опустеет
        """
        updated_at = self._updated_at
        now = datetime.utcnow()
        if self._capacity == 0 and updated_at is not None and updated_at + self.rule.interval > now:
            return updated_at + self.rule.interval - now
        return None

    def commit_request(self):
        """
        Обновляет значения в кэше, относящиеся к данному ведру.
        Если в кэше ведра нет, создаём его с текущим timestamp и ёмкостью, меньшей максимальной на 1.
        Если ведро обновлялось раньше, чем истёк его интервал действия, наращиваем его ёмкость и обновляем дату обновления.
        Если ведро актуально, уменьшаем его ёмкость на 1.

        Мы предполагаем, что пользователь не злоумышленник, поэтому даём ему возможность совершать больше
        реквестов в отведённый интервал, если у ведра осталась неиспользованная емкость и задан periods_to_overtake > 0.
        Сделав таймаут кэша равным нескольким интервалам действия ведра, мы
        ограничим возможность наверстать его неиспользованную ёмкость.
        """

        cache_interval = self.rule.interval.total_seconds() * (self.options.periods_to_overtake + 1)
        cache_interval = max(int(cache_interval), 1)
        updated_at = self._updated_at
        max_capacity = self.rule.max_requests - 1
        now = datetime.utcnow()

        if updated_at is None:
            # во избежание одновременного присвоения значения ёмкости из нескольких потоков,
            # мы сначала пробуем нарастить ёмкость ведра
            self._log('create', self.base_key, 'for', cache_interval, '(%d capacity)' % max_capacity)
            if self._capacity is None or self._redis.hincrby(self.base_key, self.updated_at_key, 1) > max_capacity:
                self._redis.hset(self.base_key, self.capacity_key, max_capacity)
                self._redis.expire(self.base_key, cache_interval)
            self._redis.hset(self.base_key, self.updated_at_key, now.timestamp())

        elif updated_at < now - self.rule.interval:
            self._log('update', self.base_key, '(+%d)' % max_capacity)
            self._redis.hmset(self.base_key, {
                self.capacity_key: (self._capacity or 0) + max_capacity,
                self.updated_at_key: now.timestamp()
            })
            self._redis.expire(self.base_key, cache_interval)
        else:
            self._log('spent', self.base_key, '%d remaining', self._capacity - 1)
            self._redis.hincrby(self.base_key, self.capacity_key, -1)
