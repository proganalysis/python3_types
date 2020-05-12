import os
import unittest
from datetime import datetime, timedelta

import collections
import mock
import pykube
import pytz
import yaml
from azure.mgmt.compute.models import VirtualMachineScaleSetVM, \
    VirtualMachineInstanceView, VirtualMachineSize, Usage, UsageName
from azure.mgmt.resource.resources.models import ResourceGroup

from autoscaler import KubePod
from autoscaler.azure import AzureVirtualScaleSet
from autoscaler.azure_api import AzureScaleSet, AzureWrapper


def _default_mock_clients(region, instances=[], quotas={'Dv2': 100, 'NC': 100}):
    sizes = [
        VirtualMachineSize(name="Standard_D1_v2", number_of_cores=1),
        VirtualMachineSize(name="Standard_NC24", number_of_cores=24)
    ]
    mock_client = mock.Mock()
    mock_client.virtual_machine_scale_set_vms = mock.Mock()
    mock_client.virtual_machine_scale_set_vms.list = mock.Mock(return_value=instances)
    mock_client.virtual_machine_scale_sets = mock.Mock()
    mock_client.virtual_machine_scale_sets.create_or_update = mock.Mock()
    mock_client.virtual_machine_scale_sets.delete_instances = mock.Mock()
    mock_client.virtual_machine_sizes = mock.Mock()
    mock_client.virtual_machine_sizes.list = mock.Mock(return_value=sizes)
    mock_client.usage = mock.Mock()
    usage_limits = []
    for k, v in quotas.items():
        usage_limits.append(Usage(name=UsageName(value="standard" + k + "Family"), limit=v, current_value=0))
    mock_client.usage.list = mock.Mock(return_value=usage_limits)

    monitor_client = mock.Mock()
    monitor_client.activity_logs = mock.Mock()
    monitor_client.activity_logs.list = mock.Mock(return_value=[])

    azure_resource_group = ResourceGroup(location=region)
    resource_client = mock.Mock()
    resource_client.resource_groups = mock.Mock()
    resource_client.activity_logs.get = mock.Mock(return_value=azure_resource_group)

    return (mock_client, monitor_client, resource_client)


class TestCluster(unittest.TestCase):
    def test_failed_scale_up(self):
        region = 'test'

        mock_client, monitor_client, resource_client = _default_mock_clients(region)

        instance_type = 'Standard_D1_v2'
        resource_group = 'test-resource-group'
        failed_scale_set = AzureScaleSet(region, resource_group, 'test-scale-set1', instance_type, 0, 'Failed')
        scale_set = AzureScaleSet(region, resource_group, 'test-scale-set2', instance_type, 0, 'Succeeded')

        virtual_scale_set = AzureVirtualScaleSet(region, resource_group, AzureWrapper(mock_client, monitor_client, resource_client), instance_type, False, [failed_scale_set, scale_set], [])

        virtual_scale_set.scale(5)

        mock_client.virtual_machine_scale_sets.create_or_update.assert_called_once()
        self.assertEqual(mock_client.virtual_machine_scale_sets.create_or_update.call_args[1]['parameters'].sku.capacity, 5)

    def test_scale_up(self):
        region = 'test'

        mock_client, monitor_client, resource_client = _default_mock_clients(region)

        instance_type = 'Standard_D1_v2'
        resource_group = 'test-resource-group'
        scale_set = AzureScaleSet(region, resource_group, 'test-scale-set', instance_type, 0, 'Succeeded')

        virtual_scale_set = AzureVirtualScaleSet(region, resource_group, AzureWrapper(mock_client, monitor_client, resource_client), instance_type, False, [scale_set], [])

        virtual_scale_set.scale(5)

        mock_client.virtual_machine_scale_sets.create_or_update.assert_called_once()
        self.assertEqual(mock_client.virtual_machine_scale_sets.create_or_update.call_args[1]['parameters'].sku.capacity, 5)

    def test_priority(self):
        region = 'test'

        mock_client, monitor_client, resource_client = _default_mock_clients(region)

        instance_type = 'Standard_D1_v2'
        resource_group = 'test-resource-group'
        scale_set = AzureScaleSet(region, resource_group, 'test-scale-set', instance_type, 0, 'Succeeded', priority=-1)
        # Name sorts lexicographically before previous scale set, but priority is after it
        scale_set2 = AzureScaleSet(region, resource_group, 'a-test-scale-set', instance_type, 0, 'Succeeded', priority=1)

        virtual_scale_set = AzureVirtualScaleSet(region, resource_group, AzureWrapper(mock_client, monitor_client, resource_client), instance_type, True, [scale_set, scale_set2], [])

        virtual_scale_set.scale(1)

        self.assertEqual(virtual_scale_set.global_priority, -1)

        self.assertEqual(mock_client.virtual_machine_scale_sets.create_or_update.call_count, 1)
        self.assertEqual(mock_client.virtual_machine_scale_sets.create_or_update.call_args_list[0][0][1], 'test-scale-set')

    def test_slow_scale_up(self):
        region = 'test'

        mock_client, monitor_client, resource_client = _default_mock_clients(region)

        instance_type = 'Standard_D1_v2'
        resource_group = 'test-resource-group'
        scale_set = AzureScaleSet(region, resource_group, 'test-scale-set', instance_type, 0, 'Succeeded')
        scale_set2 = AzureScaleSet(region, resource_group, 'test-scale-set2', instance_type, 0, 'Succeeded')

        virtual_scale_set = AzureVirtualScaleSet(region, resource_group, AzureWrapper(mock_client, monitor_client, resource_client), instance_type, True, [scale_set, scale_set2], [])

        virtual_scale_set.scale(2)

        self.assertEqual(mock_client.virtual_machine_scale_sets.create_or_update.call_count, 2)
        self.assertEqual(mock_client.virtual_machine_scale_sets.create_or_update.call_args_list[0][1]['parameters'].sku.capacity, 1)
        self.assertEqual(mock_client.virtual_machine_scale_sets.create_or_update.call_args_list[1][1]['parameters'].sku.capacity, 1)

    def test_tainted_scale_set(self):
        region = 'test'

        mock_client, monitor_client, resource_client = _default_mock_clients(region)

        instance_type = 'Standard_NC24'
        resource_group = 'test-resource-group'
        scale_set = AzureScaleSet(region, resource_group, 'test-scale-set', instance_type, 0, 'Succeeded', no_schedule_taints={'gpu': 'yes'})

        virtual_scale_set = AzureVirtualScaleSet(region, resource_group, AzureWrapper(mock_client, monitor_client, resource_client), instance_type, True, [scale_set], [])

        dir_path = os.path.dirname(os.path.realpath(__file__))
        with open(os.path.join(dir_path, 'data/busybox.yaml'), 'r') as f:
            dummy_pod = yaml.load(f.read())
        pod = KubePod(pykube.Pod(None, dummy_pod))

        self.assertFalse(virtual_scale_set.is_taints_tolerated(pod))

        dummy_pod['spec']['tolerations'] = [{'key': 'gpu', 'operator': 'Exists'}]
        pod = KubePod(pykube.Pod(None, dummy_pod))
        self.assertTrue(virtual_scale_set.is_taints_tolerated(pod))

    def test_out_of_quota(self):
        region = 'test'

        mock_client, monitor_client, resource_client = _default_mock_clients(region)

        instance_type = 'Standard_D1_v2'
        resource_group = 'test-resource-group'
        scale_set = AzureScaleSet(region, resource_group, 'test-scale-set', instance_type, 0, 'Succeeded',
                                  timeout_until=datetime.now(pytz.utc) + timedelta(minutes=10), timeout_reason="fake reason")
        virtual_scale_set = AzureVirtualScaleSet(region, resource_group, AzureWrapper(mock_client, monitor_client, resource_client), instance_type, False, [scale_set], [])
        self.assertTrue(virtual_scale_set.is_timed_out())

    def test_near_quota_limit(self):
        region = 'test'

        mock_client, monitor_client, resource_client = _default_mock_clients(region, quotas={'Dv2': 5})

        instance_type = 'Standard_D1_v2'
        resource_group = 'test-resource-group'
        scale_set = AzureScaleSet(region, resource_group, 'test-scale-set', instance_type, 0, 'Succeeded')

        virtual_scale_set = AzureVirtualScaleSet(region, resource_group, AzureWrapper(mock_client, monitor_client, resource_client), instance_type, False, [scale_set], [])

        virtual_scale_set.scale(10)

        mock_client.virtual_machine_scale_sets.create_or_update.assert_called_once()
        self.assertEqual(mock_client.virtual_machine_scale_sets.create_or_update.call_args[1]['parameters'].sku.capacity, 5)

    def test_scale_in(self):
        region = 'test'
        resource_group = 'test-resource-group'

        instance = VirtualMachineScaleSetVM(location=region)
        instance.vm_id = 'test-vm-id'
        instance.instance_id = 0
        instance.instance_view = VirtualMachineInstanceView()
        instance.instance_view.statuses = []

        mock_client, monitor_client, resource_client = _default_mock_clients(region, instances=[instance])

        TestNode = collections.namedtuple('TestNode', ['instance_id', 'unschedulable'])
        test_node = TestNode(instance_id=instance.vm_id, unschedulable=False)

        instance_type = 'Standard_D1_v2'
        scale_set = AzureScaleSet(region, resource_group, 'test-scale-set', instance_type, 1, 'Succeeded')

        virtual_scale_set = AzureVirtualScaleSet(region, resource_group, AzureWrapper(mock_client, monitor_client, resource_client), instance_type, False, [scale_set], [test_node])

        self.assertEqual(virtual_scale_set.instance_ids, {instance.vm_id})
        self.assertEqual(virtual_scale_set.nodes, [test_node])

        virtual_scale_set.scale_nodes_in([test_node])
        mock_client.virtual_machine_scale_sets.delete_instances.assert_called_once_with(resource_group, scale_set.name, [instance.instance_id])
