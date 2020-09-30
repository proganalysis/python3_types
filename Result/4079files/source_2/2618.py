

# require pytagcloud version 0.3.5
# require pygame version 1.9.3
# simplejson version 3.10.0

import random
import pytagcloud
import webbrowser

r = lambda: random.randint(0,255)
color = lambda: (r(), r(), r())

def get_tags(nouns_data:list, multiplier:int = 5):
    r = []
    for word in nouns_data:
        if int(word[1]) >=8 :
            r.append({'color':color(), 'tag':word[0], 'size':word[1]*multiplier})

    return r



def draw_cloud(tags:list, filename:str, fontname:str='D2Coding', size= (1920, 1080)):
    pytagcloud.create_tag_image(tags ,filename,fontname=fontname, size=size, rectangular=True)
    webbrowser.open(filename)


