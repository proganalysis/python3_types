# !/usr/bin/env python
# -*- encoding: utf-8 -*-
# vim: set et sw=4 ts=4 sts=4 ff=unix fenc=utf8:
# Author: Vincent<vincent8280@outlook.com>
#         http://wax8280.github.io
# Created on 2017/10/10 14:05
import os
import re
import time
from copy import deepcopy
from queue import Queue, PriorityQueue
from urllib.parse import urlparse
from bs4 import BeautifulSoup

from web2kindle import MAIN_CONFIG, CONFIG_ZHIHU_ZHUANLAN, INF
from web2kindle.libs.content_formating import format_zhihu_content
from web2kindle.libs.crawler import Crawler, RetryDownload, Task
from web2kindle.libs.db import ArticleDB
from web2kindle.libs.html2kindle import HTML2Kindle
from web2kindle.libs.send_email import SendEmail2Kindle
from web2kindle.libs.utils import write, md5string, load_config, check_config, make_crawler_meta, read_file_to_list
from web2kindle.libs.log import Log

__all__ = ["main"]

DESC = {
    'script_args': {'script_name': 'zhihu_zhuanlan',
                    'script_introduction': '获取知乎专栏',
                    'i': (True, '专栏名称'),
                    'start': True,
                    'img': True,
                    'gif': True,
                    'email': True, },
    'script_config': {
        'script_name': 'zhihu_zhuanlan',
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
    'kw': "[{name: 'window', default: 50, select: null}],"
}

LOG = Log("zhihu_zhuanlan")
SCRIPT_CONFIG = load_config(CONFIG_ZHIHU_ZHUANLAN)
DEFAULT_HEADERS = {
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/'
                  '61.0.3163.100 Safari/537.36'
}
ARTICLE_ID_SET = set()
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
        zhihu_zhuanlan_main([i], int(start), int(end), kw)
    elif f:
        zhuanlan_list = read_file_to_list(f)
        if not isinstance(zhuanlan_list, list):
            zhuanlan_list = [zhuanlan_list]
        zhihu_zhuanlan_main(zhuanlan_list, start, end, kw)


def zhihu_zhuanlan_main(zhuanlan_name_list, start, end, kw):
    LOG.logd("META:{}".format(META))
    LOG.logd("SCRIPT_CONFIG:{}".format(SCRIPT_CONFIG))
    check_config(MAIN_CONFIG, SCRIPT_CONFIG, 'SAVE_PATH', LOG)

    iq, oq, result_q = PriorityQueue(), PriorityQueue(), Queue()
    crawler = Crawler(iq, oq, result_q, MAIN_CONFIG.get('PARSER_WORKER', 1), MAIN_CONFIG.get('DOWNLOADER_WORKER', 1),
                      MAIN_CONFIG.get('RESULTER_WORKER', 1))

    for zhuanlan_name in zhuanlan_name_list:
        if not META:
            new_header = deepcopy(DEFAULT_HEADERS)
            m_meta = {'headers': new_header}
        else:
            m_meta = deepcopy(META)
        m_meta['headers']['Referer'] = 'https://zhuanlan.zhihu.com/{}'.format(zhuanlan_name)
        m_meta['verify'] = False

        save_path = os.path.join(SCRIPT_CONFIG['SAVE_PATH'], str(zhuanlan_name))

        task = Task.make_task({
            'url': 'https://zhuanlan.zhihu.com/api/columns/{}/posts?limit=20&offset={}'.format(zhuanlan_name, start),
            'method': 'GET',
            'meta': m_meta,
            'parser': parser_list,
            'priority': 0,
            'save': {'cursor': start,
                     'save_path': save_path,
                     'start': start,
                     'end': end,
                     'kw': kw,
                     'name': zhuanlan_name},
            'retry': 10,
            'retry_delay': 10
        })

        iq.put(task)
        # Init DB
        with ArticleDB(save_path, VERSION=0) as db:
            db.insert_meta_data(['BOOK_NAME', zhuanlan_name])
            _ = db.select_all_article_id()
        if _:
            for each in _:
                ARTICLE_ID_SET.add(each[0])

    crawler.start()
    for zhuanlan_name in zhuanlan_name_list:
        items = []
        save_path = os.path.join(SCRIPT_CONFIG['SAVE_PATH'], str(zhuanlan_name))
        book_name = '知乎专栏_{}'.format(zhuanlan_name)
        with ArticleDB(save_path, VERSION=0) as db:
            items.extend(db.select_article())
            db.increase_version()
            db.reset()

        if items:
            with HTML2Kindle(items, save_path, book_name, MAIN_CONFIG.get('KINDLEGEN_PATH')) as html2kindle:
                html2kindle.make_metadata(window=kw.get('window', 50))
                html2kindle.make_book_multi(save_path)

            if kw.get('email'):
                with SendEmail2Kindle() as s:
                    s.send_all_mobi(os.path.join(SCRIPT_CONFIG['SAVE_PATH'], str(zhuanlan_name)))
        else:
            LOG.log_it('无新项目', 'INFO')


def parser_list(task):
    response = task['response']
    new_tasks = []
    to_next = True

    if not response:
        raise RetryDownload

    try:
        data = response.json()
        data.reverse()
    except Exception as e:
        LOG.log_it('解析JSON出错（如一直出现，而且浏览器能正常访问知乎，可能是知乎代码升级，请通知开发者。）ERRINFO:{}'
                   .format(str(e)), 'WARN')
        raise RetryDownload

    for item in data:
        # 如果在数据库里面已经存在的项目，就不继续爬了
        url = 'https://zhuanlan.zhihu.com' + item['url']
        if md5string(url) in ARTICLE_ID_SET:
            to_next = False
            continue

        m_mate = deepcopy(task['meta'])
        m_mate['headers'][
            'Accept'] = "text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,image/apng,*/*;q=0.8"

        new_task = Task.make_task({
            'url': url,
            'method': 'GET',
            'meta': m_mate,
            'parser': parser_content,
            'resulter': resulter_content,
            'priority': 5,
            'save': task['save'],
            'title': item['title'],
        })
        new_tasks.append(new_task)

    # 下一页
    if to_next and len(data) != 0:
        if task['save']['cursor'] < task['save']['end'] - 20:
            next_page_task = deepcopy(task)
            next_page_task.update(
                {'url': re.sub('offset=\d+', 'offset={}'.format(task['save']['cursor'] + 20), next_page_task['url'])})
            next_page_task['save'].update({'cursor': next_page_task['save']['cursor'] + 20})
            new_tasks.append(next_page_task)

    return None, new_tasks


def parser_content(task):
    title = task['title']
    new_tasks = []

    response = task['response']
    if not response:
        raise RetryDownload

    bs = BeautifulSoup(response.text, HTML_PARSER_NAME)

    content_tab = bs.select('.Post-RichText')
    if content_tab:
        content = str(content_tab[0])
    else:
        LOG.log_it("不能找到文章的内容。（如一直出现，而且浏览器能正常访问知乎，可能是知乎代码升级，请通知开发者。）", 'WARN')
        raise RetryDownload

    author_name = bs.select('.PostIndex-authorName')[0].string if bs.select('.PostIndex-authorName') else ''
    voteup_count = re.search('likesCount&quot;:(\d+),', response.text).group(1) if re.search(
        'likesCount&quot;:(\d+),', response.text) else ''
    created_time = str(bs.select('.PostIndex-header .HoverTitle')[1]['data-hover-title']) if len(
        bs.select('.PostIndex-header .HoverTitle')) == 2 else ''
    article_url = task['url']

    download_img_list, content = format_zhihu_content(content, task, HTML_PARSER_NAME)

    item = [md5string(article_url), title, content, created_time, voteup_count, author_name,
            int(time.time() * 100000)]

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


"""
在convert_link函数里面md5(url)，然后转换成本地链接
在resulter_downloader_img函数里面，将下载回来的公式，根据md5(url)保存为文件名
"""


def resulter_downloader_img(task):
    if 'www.zhihu.com/equation' not in task['url']:
        write(os.path.join(task['save']['save_path'], 'static'), urlparse(task['response'].url).path[1:],
              task['response'].content, mode='wb')
    else:
        write(os.path.join(task['save']['save_path'], 'static'), md5string(task['url']) + '.svg',
              task['response'].content,
              mode='wb')
