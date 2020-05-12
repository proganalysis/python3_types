"""项目管理"""
import copy
import random
from . import workers
from collections import deque
from pyloom.server import web, response as R
from pyloom.common import Logger, PickleContainer, now

logger = Logger.instance('pyloom')


class PickleDriver(object):
    _count = 0
    _max_count = 5
    _next_pop_time = {}  # project_id:timestamp

    def __init__(self, path):
        self._db: dict = PickleContainer.instance(path, 'queues', {})

    def create(self, project_id, seeders, timeout, interval, results_mode):
        """创建队列"""
        if project_id in self._db:
            raise R.Conflict(f"已存在的project_id:{project_id}")
        self._db[project_id] = {
            'queues': {
                'waiting-deques': (deque(seeders), deque(), deque()),
                'waiting-set': dict.fromkeys(seeders, None),  # set无法pickle
                'processing': {},
                'errors': {},
                'results': {}
            },
            'timeout': timeout,
            'interval': interval,
            'results_mode': results_mode
        }

    def get_projects(self):
        """所有队列"""
        return list(self._db.keys())

    def modify_options(self, project_id, timeout, interval):
        """修改配置"""
        if project_id not in self._db:
            raise R.NotFound(f"未找到project_id:{project_id}")
        self._db[project_id]['timeout'] = timeout
        self._db[project_id]['interval'] = interval

    def exist(self, project_id, url, url_hash):
        """URL是否重复"""
        if project_id not in self._db:
            raise R.NotFound(f"未找到project_id:{project_id}")
        queues = self._db[project_id]['queues']
        if url_hash in queues['results']:
            return 'results'
        elif url in queues['processing']:
            return 'processing'
        elif url in queues['waiting-set']:
            return 'waiting-set'
        else:
            for tag in queues['errors']:
                if url in queues['errors'][tag]:
                    return 'errors'
            return None

    def add(self, project_id, urls: dict, priority):
        """入队"""
        if project_id not in self._db:
            raise R.NotFound(f"未找到project_id:{project_id}")
        queues = self._db[project_id]['queues']
        queue_names = []
        for url, url_hash in urls.items():
            queue_name = self.exist(project_id, url, url_hash)
            if queue_name is None:  # 若未重复
                queues['waiting-deques'][priority].appendleft(url)  # 左进右出
                queues['waiting-set'][url] = url_hash
            queue_names.append(queue_name)
        return queue_names

    def pop(self, projects, limit=10):
        """弹出"""
        if limit == 0:
            limit = 10
        urls = []
        n = now()
        projects_random = copy.deepcopy(projects)
        random.shuffle(projects_random)
        for project_id in projects_random:  # 随机挑选项目
            if project_id not in self._db:
                continue
            queues = self._db[project_id]['queues']
            interval = self._db[project_id]['interval']
            # 间隔控制
            if project_id in PickleDriver._next_pop_time:
                expire_at = PickleDriver._next_pop_time[project_id]
                if expire_at > n:
                    continue
                else:
                    del PickleDriver._next_pop_time[project_id]
            # 按优先级遍历队列
            for dq in queues['waiting-deques']:
                while True:
                    if len(dq) == 0:
                        break  # 队列空了，换下一队列
                    else:
                        url = dq.pop()  # 等待队列中弹出（左进右出）
                        urls.append(url)
                        url_hash = queues['waiting-set'].pop(url)  # 等待队列排重器中删除
                        queues['processing'][url] = (n, url_hash)  # 进行队列中加入
                        # 弹出间隔控制
                        if interval:
                            PickleDriver._next_pop_time[project_id] = n + interval
                        if len(urls) >= limit:
                            return urls
        self._flush()
        # 弹出量未达到max_count
        return urls

    def _flush(self):
        """清洗进行队列中的超时项"""
        # 控制清洗节奏
        PickleDriver._count += 1
        if PickleDriver._count < PickleDriver._max_count:
            return
        # 清洗
        for project_id, value in self._db.items():
            processing = value['queues']['processing']
            timeout = value['timeout']
            n = now()
            urls = []
            for url, (time_start, _) in processing.items():
                expire_at = time_start + timeout
                if expire_at < n:
                    logger.debug("超时", url, n - expire_at)
                    urls.append(url)
                else:
                    logger.debug("未超时", url, expire_at - n)
            for url in urls:
                self.report_error(project_id, url, 'timeout')
            logger.debug(f"在{project_id}.processing中清理了{len(urls)}个超时URL")
        PickleDriver._count = 0

    def report_finish(self, project_id, url):
        """完成"""
        if project_id not in self._db:
            raise R.NotFound(f"未找到project_id:{project_id}")
        queues = self._db[project_id]['queues']
        if url in queues['processing']:
            _, url_hash = queues['processing'].pop(url)
            queues['results'][url_hash] = None

    def report_error(self, project_id, url, tag):
        """异常"""
        if project_id not in self._db:
            raise R.NotFound(f"未找到project_id:{project_id}")
        queues = self._db[project_id]['queues']
        if url in queues['processing']:
            _, url_hash = queues['processing'].pop(url)
            q = queues['errors'].setdefault(tag, [])
            if url not in q:
                q.append((url, url_hash))

    def get_queues(self, project_id):
        """获取队列信息"""
        if project_id not in self._db:
            raise R.NotFound(f"未找到project_id:{project_id}")
        queues = self._db[project_id]['queues']
        return {
            'queues': {
                'waiting': [len(q) for q in queues['waiting-deques']],
                'processing': len(queues['processing']),
                'errors': sum([len(q) for q in queues['errors'].values()]),
                'results': len(queues['results'])
            },
            'timeout': self._db[project_id]['timeout'],
            'interval': self._db[project_id]['interval'],
            'results_mode': self._db[project_id]['results_mode'],
        }

    def get_error_tags(self, project_id):
        """获取异常标签"""
        if project_id not in self._db:
            raise R.NotFound(f"未找到project_id:{project_id}")
        queues = self._db[project_id]['queues']
        return {tag: len(q) for tag, q in queues['errors'].items()}

    def get_error_urls(self, project_id, tag, start=0, limit=0):
        """获取异常标签下的URL"""
        if project_id not in self._db:
            raise R.NotFound(f"未找到project_id:{project_id}")
        queues = self._db[project_id]['queues']
        if tag not in queues['errors']:
            raise R.NotFound(f'未找到tag:{tag}')
        if limit:
            return [items[0] for items in queues['errors'][tag][start: start + limit]]
        else:
            return [items[0] for items in queues['errors'][tag][start:]]

    def rollback_errors(self, project_id, tag, priority):
        """回滚异常队列"""
        if project_id not in self._db:
            raise R.NotFound(f"未找到project_id:{project_id}")
        queues = self._db[project_id]['queues']
        if tag not in queues['errors']:
            raise R.NotFound(f'未找到tag:{tag}')
        urls = dict(queues['errors'].pop(tag))
        return self.add(project_id, urls, priority)

    def remove(self, project_id):
        """移除队列"""
        if project_id not in self._db:
            raise R.NotFound(f"未找到project_id:{project_id}")
        del self._db[project_id]


class MongoDriver(object):
    def create(self, project_id, seeders, timeout, interval, results_mode):
        """创建队列"""
        raise R.ServiceUnavailable("未实现")

    def get_projects(self):
        """所有队列"""
        raise R.ServiceUnavailable("未实现")

    def modify_options(self, project_id, timeout, interval):
        """修改配置"""
        raise R.ServiceUnavailable("未实现")

    def exist(self, project_id, url, url_hash):
        """URL是否重复"""
        raise R.ServiceUnavailable("未实现")

    def add(self, project_id, urls: dict, priority):
        """入队"""
        raise R.ServiceUnavailable("未实现")

    def pop(self, projects, limit=10):
        """弹出"""
        raise R.ServiceUnavailable("未实现")

    def report_finish(self, project_id, url):
        """完成"""
        raise R.ServiceUnavailable("未实现")

    def report_error(self, project_id, url, tag):
        """异常"""
        raise R.ServiceUnavailable("未实现")

    def get_queues(self, project_id):
        """获取队列信息"""
        raise R.ServiceUnavailable("未实现")

    def get_error_tags(self, project_id):
        """获取异常标签"""
        raise R.ServiceUnavailable("未实现")

    def get_error_urls(self, project_id, tag, start=0, limit=0):
        """获取异常标签下的URL"""
        raise R.ServiceUnavailable("未实现")

    def rollback_errors(self, project_id, tag, priority):
        """回滚异常队列"""
        raise R.ServiceUnavailable("未实现")

    def remove(self, project_id):
        """移除队列"""
        raise R.ServiceUnavailable("未实现")


class _BaseHandler(web.BaseHandler):
    def __init__(self, *args, **kwargs):
        super(_BaseHandler, self).__init__(*args, **kwargs)
        if self.application.options.debug:
            self.worker_driver = workers.PickleDriver(self.application.configs['pickle'])
            self.driver = PickleDriver(self.application.configs['pickle'])
        else:
            self.worker_driver = workers.MongoDriver()
            self.driver = MongoDriver()


class QueuesHandler(_BaseHandler):
    def post(self):
        """创建队列"""
        project_id = self.json.str("project_id")
        seeders = self.json.list("seeders")
        timeout = self.json.int("timeout", left=1)
        interval = self.json.int("interval", left=0)
        results_mode = self.json.str("results_mode")
        self.driver.create(project_id, seeders, timeout, interval, results_mode)
        return R.NoContent()

    def get(self):
        """获取所有队列"""
        return R.OK({
            "projects": self.driver.get_projects()
        })


class QueueHandler(_BaseHandler):
    def get(self, project_id):
        """获取队列信息"""
        return R.OK(self.driver.get_queues(project_id))

    def delete(self, project_id):
        """删除队列"""
        self.driver.remove(project_id)
        return R.NoContent()

    def patch(self, project_id):
        """修改配置"""
        timeout = self.json.int("timeout", left=1)
        interval = self.json.int("interval", left=0)
        self.driver.modify_options(project_id, timeout, interval)
        return R.NoContent()


class QueueURLsHandler(_BaseHandler):
    def post(self, project_id):
        """URL入队"""
        urls = self.json.dict("urls")
        priority = self.json.int("priority", left=0, right=3)
        duplicate = self.driver.add(project_id, urls, priority)
        return R.OK({
            'duplicate': duplicate
        })

    def patch(self, project_id):
        """修改URL状态"""
        action = self.json.str("action", options=['finish', 'error', 'pop'])

        if action == "pop" and project_id == "all":
            return self.pop()
        elif action == "finish":
            return self.report_finish(project_id)
        elif action == "error":
            return self.report_error(project_id)
        else:
            return R.Forbidden(f"未实现的action:{action}")

    def pop(self):
        """弹出URL"""
        worker_id = self.json.str("worker_id")
        limit = self.json.int("limit", left=0, default=0)
        projects = self.worker_driver.get_projects(worker_id)
        return R.OK({
            "urls": self.driver.pop(projects, limit)
        })

    def report_finish(self, project_id):
        """报告完成"""
        url = self.json.str("url")
        self.driver.report_finish(project_id, url)
        return R.NoContent()

    def report_error(self, project_id):
        """报告异常"""
        url = self.json.str("url")
        tag = self.json.str("tag")
        self.driver.report_error(project_id, url, tag)
        return R.NoContent()


class ErrorsHandler(_BaseHandler):
    def get(self, project_id):
        """获取异常标签"""
        return R.OK({
            "tags": self.driver.get_error_tags(project_id)
        })


class ErrorHandler(_BaseHandler):
    def get(self, project_id, tag):
        """获取异常队列"""
        start = self.query.int("start", default=0)
        limit = self.query.int("limit", default=0)

        return R.OK({
            "urls": self.driver.get_error_urls(project_id, tag, start, limit)
        })

    def patch(self, project_id, tag):
        """修改URL状态"""
        action = self.json.str("action", options=["rollback"])
        if action == "rollback":
            return self.rollback(project_id, tag)
        else:
            return R.Forbidden(f"未实现的action:{action}")

    def rollback(self, project_id, tag):
        """回滚异常队列"""
        priority = self.json.int("priority")
        duplicate = self.driver.rollback_errors(project_id, tag, priority)
        return R.OK({
            "duplicate": duplicate
        })
