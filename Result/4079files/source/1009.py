#!/home/md98/bamboo_env/bin python
# -*- coding: UTF-8 -*-

import random
import pytagcloud
import webbrowser

r = lambda: random.randint(0,255)
color = lambda: (r(), r(), r())

def getTags(nouns_data:list, multiplier:int = 5):
    r = []
    for word in nouns_data:
        if int(word[1]) >=8 :
            r.append({'color':color(), 'tag':word[0], 'size':word[1]*multiplier})

    return r



def drawCloud(tags:list, filename:str, fontname:str= 'D2Coding', size= (1920, 1080)):
    pytagcloud.create_tag_image(tags ,filename,fontname=fontname, size=size)
    webbrowser.open(filename)


