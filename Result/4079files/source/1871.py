# Copyright (C) 2017 Jakob Kreuze, All Rights Reserved.
#
# This file is part of Chandere.
#
# Chandere is free software: you can redistribute it and/or modify it
# under the terms of the GNU General Public License as published by the
# Free Software Foundation, either version 3 of the License, or (at your
# option) any later version.
#
# Chandere is distributed in the hope that it will be useful, but
# WITHOUT ANY WARRANTY; without even the implied warranty of
# MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE. See the GNU General
# Public License for more details.
#
# You should have received a copy of the GNU General Public License along
# with Chandere. If not, see <http://www.gnu.org/licenses/>.

"""Scraper for 4chan.org"""

__author__ = "Jakob L. Kreuze <jakob@memeware.net>"
__licence__ = "GPLv3"
__version__ = "0.3.0"

from urllib.parse import quote
import html

import aiohttp

from chandere.errors import ChandereError, check_http_status
from chandere.websites._common import contains_uri_scheme, parse_crosslink
from chandere.websites._common import parse_imageboard_uri_factory

FIELD_NAMES = ["id", "time_posted", "name", "title", "comment", "filename"]

API_BASE = "https://a.4cdn.org"
RES_BASE = "https://i.4cdn.org"

parse_uri = parse_imageboard_uri_factory("org", "thread")


def _catalog_url(board: str) -> str:
    return API_BASE + "/{}/catalog.json".format(quote(board))


def _thread_url(board: str, thread: str) -> str:
    return API_BASE + "/{}/thread/{}.json".format(board, thread)


def _file_url(board: str, tim: str, ext: str) -> str:
    return RES_BASE + "/{}/{}.{}".format(board, tim, ext)


def _tidy_post_fields(post: dict):
    post["id"] = post.get("no")
    post["time_posted"] = post.get("time")
    post["title"] = post.get("sub")
    post["comment"] = html.unescape(post.get("com", ""))
    if "ext" in post and post["ext"][0] == ".":
        post["ext"] = post["ext"][1:]

    # del post["no"]
    # del post["time"]
    # del post["sub"]
    # del post["com"]


def _threads_from_page(page: dict) -> list:
    return [int(thread.get("no")) for thread in page.get("threads")]


async def _collect_threads(board: str):
    uri = _catalog_url(board)
    async with aiohttp.ClientSession() as session:
        async with session.get(uri) as response:
            check_http_status(response.status, uri)
            for page in await response.json():
                if "threads" not in page:
                    continue
                for thread in _threads_from_page(page):
                    yield thread


async def _collect_posts_thread(board: str, thread: str):
    uri = _thread_url(board, thread)
    async with aiohttp.ClientSession() as session:
        async with session.get(uri) as response:
            check_http_status(response.status, uri)
            json = await response.json()
            for post in json.get("posts", []):
                _tidy_post_fields(post)
                yield post


async def _collect_posts_board(board: str):
    async for thread in _collect_threads(board):
        for post in _collect_posts_thread(board, thread):
            yield post


async def _collect_files_thread(board: str, thread: int):
    async for post in _collect_posts_thread(board, thread):
        if "tim" in post and "filename" in post and "ext" in post:
            url = _file_url(board, post.get("tim"), post.get("ext"))
            yield (post, url)


async def _collect_files_board(board: str):
    async for thread in _collect_threads(board):
        async for resource in _collect_files_thread(board, thread):
            yield resource


def collect_files(target: tuple):
    board, thread = target
    if thread is not None:
        return _collect_files_thread(board, thread)
    return _collect_files_board(board)


def collect_posts(target: tuple):
    board, thread = target
    if thread is not None:
        return _collect_posts_thread(board, thread)
    return _collect_posts_board(board)


def parse_target(target: str) -> tuple:
    parse = parse_uri if contains_uri_scheme(target) else parse_crosslink
    board, thread = parse(target)
    if board is None:
        raise ChandereError("Invalid target '{}'".format(target))
    return (board, thread)
