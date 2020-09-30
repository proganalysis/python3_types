import os
import requests
from ..common import Logger
from urllib.parse import urljoin

logger = Logger.instance("pyloom")


class HTTPError(Exception):
    """接口返回了错误"""

    def __init__(self, status, message):
        self.status = status
        self.message = message

    def __repr__(self):
        return f"HTTPError({self.status}, {self.message})"


class API(object):
    def __init__(self, scheduler_url):
        self._scheduler_url = scheduler_url

    def _url(self, path):
        return urljoin(self._scheduler_url, path)


class Queues(API):
    def create(self, project_id, seeders, timeout, interval, results_mode, exist_ok=False):
        """
        创建队列
        当exist_ok==True时，忽略409错误（队列已存在）
        """
        resp = requests.post(self._url("/v1/queues"), json={
            "project_id": project_id,
            "seeders": seeders,
            "timeout": timeout,
            "interval": interval,
            "results_mode": results_mode,
        })
        if resp.status_code // 100 == 2:
            return
        elif resp.status_code == 409 and exist_ok:
            return
        else:
            raise HTTPError(resp.status_code, resp.text)

    def pop_urls(self, worker_id, limit) -> list:
        """弹出一组urls"""
        resp = requests.patch(self._url("/v1/queues/all/urls"), json={
            "action": "pop",
            "worker_id": worker_id,
            "limit": limit
        })
        if resp.status_code // 100 == 2:
            return resp.json()["urls"]
        else:
            raise HTTPError(resp.status_code, resp.text)

    def add_urls(self, project_id, urls, priority) -> list:
        """批量添加URL到等待队列，返回urls重复情况"""
        resp = requests.post(self._url(f"/v1/queues/{project_id}/urls"), json={
            "action": "add",
            "urls": urls,
            "priority": priority
        })
        if resp.status_code // 100 == 2:
            return resp.json()["duplicate"]
        else:
            raise HTTPError(resp.status_code, resp.text)

    def report_finish(self, project_id, url):
        """报告URL已处理完成"""
        resp = requests.patch(self._url(f"/v1/queues/{project_id}/urls"), json={
            "action": "finish",
            "url": url
        })
        if resp.status_code // 100 != 2:
            raise HTTPError(resp.status_code, resp.text)

    def report_error(self, project_id, url, tag):
        """报告URL处理时出现异常"""
        resp = requests.patch(self._url(f"/v1/queues/{project_id}/urls"), json={
            "action": "error",
            "url": url,
            "tag": tag
        })
        if resp.status_code // 100 != 2:
            raise HTTPError(resp.status_code, resp.text)


class Workers(API):
    def create(self, name) -> str:
        """创建节点，返回worker_id"""
        resp = requests.post(self._url("/v1/workers"), json={
            "name": name
        })
        if resp.status_code // 100 == 2:
            return resp.json()["worker_id"]
        else:
            raise HTTPError(resp.status_code, resp.text)

    def patch_projects(self, worker_id, projects):
        """更新就绪列表"""
        resp = requests.patch(self._url(f"/v1/workers/{worker_id}/projects"), json={
            "projects": projects
        })
        if resp.status_code // 100 != 2:
            raise HTTPError(resp.status_code, resp.text)


class Projects(API):
    def create(self, name) -> str:
        """创建项目，返回project_id"""
        resp = requests.post(self._url("/v1/projects"), json={
            "name": name
        })
        if resp.status_code // 100 == 2:
            return resp.json()["project_id"]
        else:
            raise HTTPError(resp.status_code, resp.text)


class Buckets(API):
    def create(self, project_id, exist_ok=False):
        """
        创建存储空间
        当exist_ok==True时，忽略409错误（空间已存在）
        """
        resp = requests.post(self._url("/v1/buckets"), json={
            "project_id": project_id
        })
        if resp.status_code // 100 == 2:
            return
        elif resp.status_code == 409 and exist_ok:
            return
        else:
            raise HTTPError(resp.status_code, resp.text)


class Client(object):
    def __init__(self, scheduler_url):
        self.queues = Queues(scheduler_url)
        self.worker = Workers(scheduler_url)
        self.projects = Projects(scheduler_url)
        self.buckets = Buckets(scheduler_url)
