#
#   Dataset creation module HTTP handlers
#   Author: Yotam Salmon
#   Last Edited: 02/02/2018
#

import keywords as kw
import nets

import cv2

# For communicating with the downloader thread we will use the message queue
import task_scheduler as ts

# Helper utilities to work with HTTP requests
from http_helper import json_post, logged_in, msg, post, querystring

# Using the handler decorator to handle HTTP requests.
from server import RequestHandler, handler

import json

pending = {}

@handler("create_dataset", "POST")
def create_dataset_handler(req):
    """
    Handler for creating a dataset on the server side.
    """
    global pending

    user = logged_in(req)
    if user is None:
        return 403, {}, msg("Not Authenticated")
    
    data = json_post(req)
    try:
        subject = data["subject"]
        description = data["description"]
        positive = data["positive"]
        negative = data["negative"]
        identifier = data["identifier"] if "identifier" in data else user.get("username") + "_" + kw.get_id(subject)

        if len(subject) < 1:
            return 400, {}, msg("Must enter a subject")

        if len(description) < 1:
            return 400, {}, msg("Must enter a description")

        if len(positive) < 3:
            return 400, {}, msg("Must enter at least 3 trigger keywords")

        if len(negative) < 3:
            return 400, {}, msg("Must enter at least 3 negative keywords")

        if len(identifier) < 1:
            return 400, {}, msg("Invalid identifier")

        obj = {
            "tasks": [],
            "done": [],
            "ready": [],
            "subject": subject,
            "description": description,
            "identifier": identifier
        }
        for w in positive:
            if not kw.exists(w):
                obj["tasks"].append(
                    ts.download(w)
                )
            else:
                obj["ready"].append(w)

        for w in negative:
            if not kw.exists(w):
                obj["tasks"].append(
                    ts.download(w)
                )
            else:
                obj["ready"].append(w)

        success, obj_name = nets.create_dataset(
            identifier,
            positive,
            negative,
            user.item_id,
            subject,
            description
        )

        obj["dbid"] = obj_name

        if not success:
            return 200, {}, msg(obj_name)

        if len(obj["tasks"]) > 0:
            pending[obj_name] = obj
            return 200, {}, json.dumps({"dataset_id": obj_name})
        else:
            nets.set_working(obj_name)
            return 200, {}, json.dumps({"dataset_id": obj_name})
    except:
        return 400, {}, msg("Content is not in the correct format or a parameter is missing")


def done_task(task):
    """
    Handles a downloaded keyword
    """
    global pending
    print(task)
    print("---")
    for _id, p in pending.items():
        if task["task_id"] in p["tasks"]:
            p["done"].append(task["keyword"])
            p["tasks"].remove(task["task_id"])
            print(_id)
            if len(p["tasks"]) == 0:
                print(nets.set_working(_id))


@handler("dataset_status", "GET")
def get_dataset_status(req):
    global pending
    
    qs = querystring(req)
    
    # Making sure the id was specified
    if "id" not in qs:
        return 400, {}, msg("ID querystring not provided")
    
    if "".join(qs["id"]) not in pending.keys():
        return 200, {}, msg("Not Found")

    cpy = json.loads(json.dumps(pending["".join(qs["id"])]))
    ds = nets.get_dataset(cpy["dbid"])
    cpy["working"] = ds.get("working")
    cpy["current"] = ts._current_keyword
    return 200, {}, json.dumps(cpy)

@handler("dataset_list", "GET")
def dataset_list_handler(req):
    
    user = logged_in(req)
    if user is None:
        return 403, {}, msg("Not Authenticated")
    
    data = {x.item_id: x.data for x in nets.get_datasets(user.item_id)}
    return 200, {}, json.dumps(data)

@handler("delete_dataset", "GET")
def delete_dataset(req):
    user = logged_in(req)
    qs = querystring(req)

    if user is None:
        return 403, {}, msg("Not Authenticated")

    if "id" not in qs:
        return 400, {}, msg("ID parameter is missing in query string")

    return nets.delete_dataset("".join(qs["id"]), user.item_id)
    
@handler("dataset")
def dataset_get(req):
    qs = querystring(req)

    if "id" not in qs:
        return 200, {}, msg("Not Found")

    ds = nets.get_dataset("".join(qs["id"]))

    if not ds:
        return 200, {}, msg("Not Found")

    return 200, {}, json.dumps(ds.data)

# Registering the event handler
ts.on_keyword_downloaded = done_task

@handler("keyword")
def keyword_handler(req):
    qs = querystring(req)

    if not "k" in qs:
        return 404, {}, ""

    img = kw.collage("".join(qs["k"]))

    if img is None:
        return 404, {}, ""

    return 200, {"Content-Type": "image/png"}, cv2.imencode(".png", img)[1]