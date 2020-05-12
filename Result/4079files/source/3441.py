#
#   Classifier evaluation module
#   Author: Yotam Salmon
#   Last Edited: 28/02/2018
#

import nLib

import cv2
import numpy as np

import json
import base64

from server import handler
from http_helper import msg, json_post, post, logged_in

classifiers = {}

def process_image(img):
    """
    Converts an arbitary image to a matrix that can be fed into a classifier.
    """
    
    # Making the image 3D
    if len(img.shape) < 3:
        img = img.reshape(img.shape[0], img.shape[1], 1)

    # Grayscaling the image
    if img.shape[2] > 1:
        img = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
    
    # Cutting the center square
    m = min(img.shape[0], img.shape[1])
    img = img[img.shape[0] // 2 - m // 2 : img.shape[0] // 2 + m // 2, img.shape[1] // 2 - m // 2 : img.shape[1] // 2 + m // 2]

    # Resizing
    img = cv2.resize(img, (nLib.IMG_SIZE, nLib.IMG_SIZE))

    return img

def classify_image(img, classifier_name):
    """
    Classifying an image
    """
    global classifiers

    try:
        X = process_image(img)
    except:
        return False, "Error while trying to process the image"
    
    if classifier_name in classifiers.keys():
        C = classifiers[classifier_name]
    else:
        try:
            C = nLib.load_classifier(classifier_name)
            classifiers[classifier_name] = C
        except:
            return False, "Error while trying to load the classifier"

    try:
        Y = C.predict(X.reshape(-1, nLib.IMG_SIZE, nLib.IMG_SIZE, 1))
    except:
        return False, "Error while trying to analyze the image"

    return True, Y[0][1] / np.sum(Y)


def load_b64img(b64):
    """
    Loads image from data uri
    """
    b64 = bytes(b64[max(0, b64.find(",") + 1):], "utf-8")
    nparr = np.fromstring(base64.b64decode(b64), np.uint8)
    img = cv2.imdecode(nparr, cv2.IMREAD_COLOR)
    return img

@handler("v", "POST")
def classify(req):
    data = json_post(req)

    #try:
    classifier_name = data["c"]
    b64url = data["i"]
    img = load_b64img(b64url)

    status, obj = classify_image(img, classifier_name)
    
    if status:
        return 200, {"Access-Control-Allow-Origin": "*"}, json.dumps({"result": float(obj)})
    else:
        return 200, {"Access-Control-Allow-Origin": "*"}, msg(obj)

    #except:
    #    return 400, {}, msg("Incorrect argumnet format")