"""项目管理"""
from pyloom.common import Logger, PickleContainer, now
from pyloom.server import web, response as R

logger = Logger.instance('pyloom')


class PickleDriver(object):
    _count = 0  # 当达到_max_count时，清理过期的键
    _max_count = 5

    def __init__(self, path):
        self._db = PickleContainer.instance(path, 'buckets', {})  # type: dict

    def create(self, project_id):
        """创建空间"""
        if project_id in self._db:
            raise R.Conflict(f"已存在的project_id:{project_id}")
        self._db[project_id] = {}

    def set(self, project_id, key, value, ttl):
        """添加键值对"""
        if project_id not in self._db:
            raise R.NotFound(f"未找到project_id:{project_id}")
        if ttl == -1:
            expire_at = -1
        else:
            expire_at = ttl + now()
        self._db[project_id][key] = (value, expire_at)
        PickleDriver._count += 1
        if PickleDriver._count > PickleDriver._max_count:
            # 清理过期键并且只在这里清理
            keys = []
            n = now()
            for key, (_, expire_at) in self._db[project_id].items():
                if expire_at != -1 and expire_at <= n:
                    keys.append(key)
            for key in keys:
                del self._db[project_id][key]
            logger.debug(f"Buckets清理了{len(keys)}个过期键")
            PickleDriver._count = 0

    def get(self, project_id, key):
        """获取键值对"""
        if project_id not in self._db:
            raise R.NotFound(f"未找到project_id:{project_id}")
        if key not in self._db[project_id]:
            raise R.NotFound(f"未找到key:{key}")
        value, expire_at = self._db[project_id][key]

        if expire_at == -1:
            return value, -1
        elif expire_at > now():
            return value, expire_at - now()
        else:
            raise R.NotFound(f"未找到key:{key}")

    def remove(self, project_id, key):
        """移除键值对"""
        if project_id not in self._db:
            raise R.NotFound(f"未找到project_id:{project_id}")
        if key not in self._db[project_id]:
            raise R.NotFound(f"未找到key:{key}")

        _, expire_at = self._db[project_id][key]

        if expire_at == -1 or expire_at > now():
            del self._db[project_id][key]
        else:
            raise R.NotFound(f"未找到key:{key}")


class MongoDriver(object):
    def create(self, project_id):
        """创建空间"""
        raise R.ServiceUnavailable("未实现")

    def set(self, project_id, key, value, ttl):
        """添加键值对"""
        raise R.ServiceUnavailable("未实现")

    def get(self, project_id, key):
        """获取键值对"""
        raise R.ServiceUnavailable("未实现")

    def remove(self, project_id, key):
        """移除键值对"""
        raise R.ServiceUnavailable("未实现")


class _BaseHandler(web.BaseHandler):
    def __init__(self, *args, **kwargs):
        super(_BaseHandler, self).__init__(*args, **kwargs)
        if self.application.options.debug:
            self.driver = PickleDriver(self.application.configs['pickle'])
        else:
            self.driver = MongoDriver()


class BucketsHandler(_BaseHandler):
    def post(self):
        """创建空间"""
        project_id = self.json.str("project_id")
        self.driver.create(project_id)
        return R.NoContent()


class KeyHandler(_BaseHandler):
    def put(self, project_id, key):
        """添加键值对"""
        value = self.json.str("value")
        ttl = self.json.int("ttl", left=-1, default=-1)
        self.driver.set(project_id, key, value, ttl)
        return R.NoContent()

    def head(self, project_id, key):
        """键是否存在"""
        _, ttl = self.driver.get(project_id, key)
        return R.NoContent(headers={
            "X-Key-TTL": ttl
        })

    def get(self, project_id, key):
        """获取键值对"""
        value, ttl = self.driver.get(project_id, key)

        return R.OK({
            "key": key,
            "value": value
        }, headers={
            "X-Key-TTL": ttl
        })

    def delete(self, project_id, key):
        """删除键值对"""
        self.driver.remove(project_id, key)
        return R.NoContent()
