# !/usr/bin/env python
# -*- encoding: utf-8 -*-
# vim: set et sw=4 ts=4 sts=4 ff=unix fenc=utf8:
# Author: Vincent<vincent8280@outlook.com>
#         http://wax8280.github.io
# Created on 2018/1/10 14:18
import os
import time
from copy import deepcopy
from queue import Queue, PriorityQueue
from urllib.parse import urlparse
from bs4 import BeautifulSoup

from web2kindle import MAIN_CONFIG, CONFIG_JIANSHU_ZHUANTI, INF
from web2kindle.libs.content_formating import format__jianshu_content
from web2kindle.libs.crawler import Crawler, RetryDownload, Task
from web2kindle.libs.db import ArticleDB
from web2kindle.libs.html2kindle import HTML2Kindle
from web2kindle.libs.send_email import SendEmail2Kindle
from web2kindle.libs.utils import write, md5string, load_config, check_config, format_file_name, make_crawler_meta, \
    read_file_to_list
from web2kindle.libs.log import Log

__all__ = ["main"]

DESC = {
    'script_args': {'script_name': 'jianshu_zhuanti',
                    'script_introduction': '获取简书专题',
                    'i': (True, '专题ID'),
                    'start': True,
                    'img': True,
                    'gif': True,
                    'email': True, },
    'script_config': {
        'script_name': 'jianshu_zhuanti',
        'configs': [{
            'config_name': 'SAVE_PATH',
            'config_introduction': "保存路径名",
            'default': '',
            'requried': False
        },
            {
                'config_name': 'HEADER',
                'config_introduction': "请求头部",
                'default': '',
                'requried': False
            },
        ]
    },
    'kw': "[{name: 'window', default: 50, select: null}, "
          "{name: 'order_by', default: 'top', select: ['top', 'commented_at', 'added_at']}],"

}

SCRIPT_CONFIG = load_config(CONFIG_JIANSHU_ZHUANTI)
LOG = Log("jianshu_zhuanti")
DEFAULT_HEADERS = {
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/'
                  '61.0.3163.100 Safari/537.36'
}
ARTICLE_ID_SET = set()
ORDER_TOP = 'top'
ORDER_COMMENT = 'commented_at'
ORDER_ADD = 'added_at'
API_URL = 'https://www.jianshu.com/c/{}?order_by={}&page={}'
BASE_URL = 'https://www.jianshu.com/c/{}'
META = make_crawler_meta(SCRIPT_CONFIG.get('HEADER', {}),
                         ['referer', 'connection', 'accept-encoding', 'If-None-Match', 'host', 'X-CSRF-Token'])
HTML_PARSER_NAME = 'lxml'


def main(i, f=None, start=1, end=INF, img=True, gif=False, email=False, **kw):
    kw.update({
        'img': img,
        'gif': gif,
        'email': email,
    })

    if i:
        jianshu_zhuanti_main([i], int(start), int(end), kw)
    elif f:
        items = read_file_to_list(f)
        if not isinstance(items, list):
            items = [items]
        jianshu_zhuanti_main(items, start, end, kw)


def jianshu_zhuanti_main(zhuanti_list, start, end, kw):
    """start默认1；end为结束页数，每页9个"""
    LOG.logd("META:{}".format(META))
    LOG.logd("SCRIPT_CONFIG:{}".format(SCRIPT_CONFIG))
    check_config(MAIN_CONFIG, SCRIPT_CONFIG, 'SAVE_PATH', LOG)

    iq, oq, result_q = PriorityQueue(), PriorityQueue(), Queue()
    crawler = Crawler(iq, oq, result_q,
                      MAIN_CONFIG.get('PARSER_WORKER', 1),
                      MAIN_CONFIG.get('DOWNLOADER_WORKER', 1),
                      MAIN_CONFIG.get('RESULTER_WORKER', 1))

    start = int(start)
    end = int(end)

    for zhuanti in zhuanti_list:
        if not META:
            new_header = deepcopy(DEFAULT_HEADERS)
            m_meta = {'headers': new_header}
        else:
            m_meta = deepcopy(META)
        m_meta['headers']['Referer'] = BASE_URL.format(zhuanti)
        m_meta['verify'] = False

        # 以专题的数字作为子文件名
        save_path = os.path.join(SCRIPT_CONFIG['SAVE_PATH'], str(zhuanti))

        if kw.get('order_by') == 'comment':
            order_by = ORDER_COMMENT
        elif kw.get('order_by') == 'add':
            order_by = ORDER_ADD
        elif kw.get('order_by') == 'top':
            order_by = ORDER_TOP
        else:
            # 默认add
            order_by = ORDER_ADD

        task = Task.make_task({
            'url': API_URL.format(zhuanti, order_by, start),
            'method': 'GET',
            'meta': m_meta,
            'parser': parser_list,
            'priority': 0,
            'save': {'cursor': start,
                     'save_path': save_path,
                     'start': start,
                     'end': end,
                     'kw': kw,
                     'name': zhuanti,
                     'order_by': order_by},
            'retry': 10,
            'retry_delay': 10
        })

        iq.put(task)

        # Init DB
        with ArticleDB(save_path, VERSION=0) as db:
            _ = db.select_all_article_id()

        # 利用集合去重
        if _:
            for each in _:
                ARTICLE_ID_SET.add(each[0])

    # 开始爬虫
    crawler.start()

    # 开始制作电子书
    for zhuanti in zhuanti_list:
        items = []
        save_path = os.path.join(SCRIPT_CONFIG['SAVE_PATH'], str(zhuanti))
        with ArticleDB(save_path, VERSION=0) as db:
            # 读取所有文章
            items.extend(db.select_article())
            # 从数据库中获取专题名字
            book_name = db.select_meta('BOOK_NAME')
            # 更新数据库版本
            db.increase_version()
            # 数据库收尾工作
            db.reset()

        if items:
            with HTML2Kindle(items, save_path, book_name, MAIN_CONFIG.get('KINDLEGEN_PATH')) as html2kindle:
                html2kindle.make_metadata(window=kw.get('window', 50))
                html2kindle.make_book_multi(save_path)

            if kw.get('email'):
                with SendEmail2Kindle() as s:
                    s.send_all_mobi(save_path)
        else:
            LOG.log_it('无新项目', 'INFO')


def parser_list(task):
    response = task['response']
    new_tasks = []
    to_next = True

    if not response:
        raise RetryDownload

    try:
        text = response.text
        bs = BeautifulSoup(text, HTML_PARSER_NAME)
    except Exception as e:
        LOG.log_it('解析网页出错（如一直出现，而且浏览器能正常访问，可能是网站网站代码升级，请通知开发者。）ERRINFO:{}'
                   .format(str(e)), 'WARN')
        raise RetryDownload

    book_name = bs.title.string if bs.title else task['save']['name']

    # 插入文集名字
    with ArticleDB(task['save']['save_path']) as article_db:
        article_db.insert_meta_data(['BOOK_NAME', format_file_name('简书专题_' + book_name)], update=False)

    # 顺序反向
    items = bs.select('a.title')
    items.reverse()

    for item in items:
        # 如果已经在数据库中，则不下载
        url = 'https://www.jianshu.com' + item.attrs['href']
        if md5string(url) in ARTICLE_ID_SET:
            to_next = False
            continue

        try:
            title = item.string
        except Exception:
            LOG.log_it('解析标题出错（如一直出现，而且浏览器能正常访问，可能是网站网站代码升级，请通知开发者。）', 'WARN')
            raise RetryDownload

        new_task = Task.make_task({
            'url': url,
            'method': 'GET',
            'meta': task['meta'],
            'parser': parser_content,
            'resulter': resulter_content,
            'priority': 5,
            'save': task['save'],
            'title': title,
        })
        new_tasks.append(new_task)

    # 下一页
    if to_next and len(items) != 0:
        if task['save']['cursor'] < task['save']['end']:
            next_page_task = deepcopy(task)
            next_page_task.update(
                {'url': API_URL.format(task['save']['name'], task['save']['order_by'], task['save']['cursor'] + 1)})
            next_page_task['save'].update({'cursor': next_page_task['save']['cursor'] + 1})
            new_tasks.append(next_page_task)

    return None, new_tasks


def parser_content(task):
    title = task['title']
    new_tasks = []

    response = task['response']
    if not response:
        raise RetryDownload

    bs = BeautifulSoup(response.text, HTML_PARSER_NAME)

    content_tab = bs.select('.show-content')
    if content_tab:
        content = str(content_tab[0])
    else:
        LOG.log_it("不能找到文章的内容。（如一直出现，而且浏览器能正常访问网站，可能是网站代码升级，请通知开发者。）", 'WARN')
        raise RetryDownload

    author_name = bs.select('.post .author .name a')[0].string if bs.select('.post .author .name a') else ''
    voteup_count = bs.select('.post .author .meta .likes-count')[0].string if bs.select(
        '.post .author .meta .likes-count') else ''
    created_time = bs.select('.post .author .meta .publish-time')[0].string if bs.select(
        '.post .author .meta .publish-time') else ''
    article_url = task['url']

    download_img_list, content = format__jianshu_content(content, task, HTML_PARSER_NAME)

    item = [md5string(article_url), title, content, created_time, voteup_count, author_name, int(time.time() * 100000)]

    if task['save']['kw'].get('img', True):
        img_header = deepcopy(DEFAULT_HEADERS)
        img_header.update({'Referer': response.url})
        for img_url in download_img_list:
            new_tasks.append(Task.make_task({
                'url': img_url,
                'method': 'GET',
                'meta': {'headers': img_header, 'verify': False},
                'parser': parser_downloader_img,
                'resulter': resulter_downloader_img,
                'save': task['save'],
                'priority': 10,
            }))

    task.update({"parsed_data": item})
    return task, new_tasks


def resulter_content(task):
    LOG.log_it("正在将任务 {} 插入数据库".format(task['tid']), 'INFO')
    with ArticleDB(task['save']['save_path']) as article_db:
        article_db.insert_article(task['parsed_data'])


def parser_downloader_img(task):
    return task, None


def resulter_downloader_img(task):
    if '.' not in urlparse(task['response'].url).path[1:]:
        name = urlparse(task['response'].url).path[1:] + '.jpg'
    else:
        name = urlparse(task['response'].url).path[1:]

    write(os.path.join(task['save']['save_path'], 'static'), name, task['response'].content, mode='wb')
