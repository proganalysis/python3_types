import os.path
import unittest

import pykube
import yaml

import autoscaler.capacity as capacity
from autoscaler.kube import KubeNode, KubePod


class TestCapacity(unittest.TestCase):
    def setUp(self):
        dir_path = os.path.dirname(os.path.realpath(__file__))
        with open(os.path.join(dir_path, 'data/busybox.yaml'), 'r') as f:
            dummy_pod = yaml.load(f.read())
        with open(os.path.join(dir_path, 'data/node.yaml'), 'r') as f:
            self.dummy_node = yaml.load(f.read())
            # KubeNode expects these to be strings
            for condition in self.dummy_node['status']['conditions']:
                condition['lastHeartbeatTime'] = str(condition['lastHeartbeatTime'])

        # this isn't actually used here
        # only needed to create the KubePod object...
        self.api = pykube.HTTPClient(pykube.KubeConfig.from_file('~/.kube/config'))

        self.dummy_pod = dummy_pod

    def test_can_fit(self):
        pod = KubePod(pykube.Pod(self.api, self.dummy_pod))
        node = KubeNode(pykube.Node(self.api, self.dummy_node))
        assert node.can_fit(pod.resources)

    def test_possible(self):
        pod = KubePod(pykube.Pod(self.api, self.dummy_pod))
        assert capacity.is_possible(pod)

    def test_impossible(self):
        self.dummy_pod['spec']['nodeSelector'] = {
            'aws/type': 't2.micro'
        }

        print(repr(self.dummy_pod['metadata']['creationTimestamp']))
        from dateutil.parser import parse as dateutil_parse
        print(dateutil_parse(self.dummy_pod['metadata']['creationTimestamp']))
        pod = KubePod(pykube.Pod(self.api, self.dummy_pod))
        assert not capacity.is_possible(pod)
