# -*- coding: utf-8 -*-
"""
    tests.cluster
    ---------------
    Test cluster of KINCluster
    :author: MaybeS(maytryark@gmail.com)
"""

import pytest

from KINCluster.core.cluster import Cluster 
from KINCluster.core.pipeline import Pipeline 
from KINCluster.core.item import Item
from KINCluster.lib.tokenizer import tokenize, stemize

import codecs

test_text = ['2016헌나1.txt', '2014헌나1.txt']
test_keyword = ['헌법판결문', '헌법판결문']
class Pipeline(Pipeline):
    def capture_item(self):
        for text, keyword in zip(test_text, test_keyword):
            with codecs.open('tests/data/' + text, 'r', 'utf-8') as f:
                content = f.read()
            yield Item(title=text,content=content,keyword=keyword,date='')
    def dress_item(self, items):
        pass

def test_cluster1() :
    """ Testing for cluster, using test data
    """
    cluster = Cluster(epoch=32, size=500, tokenizer="tokenize")
    pipeline = Pipeline()
    for item in pipeline.capture_item():
        cluster.put_item(item)
    cluster.cluster()

    # assert '캠프' in list(map(list, zip(*cluster.similar('노무현'))))[0]
    # assert '사건' in list(map(list, zip(*cluster.similar('박근혜'))))[0]
    
    assert len(cluster.clusters) == len(test_text)
    assert cluster.vectors.shape == (len(test_text), 500)

    assert len(cluster.unique) <= len(test_text)
    assert len(cluster.unique) == len(cluster.dumps)

    for dump in cluster.dumps:
        items, vectors, counter = zip(*dump)

        for item in items:
            assert isinstance(item, Item)

        pipeline.dress_item(items)