import http
import logging
from typing import List, Tuple, MutableMapping
from datetime import datetime

import re
from requests.packages.urllib3 import Retry

import autoscaler.utils as utils
from autoscaler.autoscaling_groups import AutoScalingGroup
from autoscaler.azure_api import AzureApi, AzureScaleSet, AzureScaleSetInstance
from autoscaler.utils import TransformingFuture, AllCompletedFuture, CompletedFuture

logger = logging.getLogger(__name__)


_RETRY_TIME_LIMIT = 30


class AzureBoundedRetry(Retry):
    """
    XXX: Azure sometimes sends us a Retry-After: 1200, even when we still have quota, causing our client to appear to hang.
    Ignore them and just retry after 30secs
    """
    def __init__(self, **kwargs):
        super().__init__(**kwargs)

    @staticmethod
    def from_retry(retry):
        new_retry = AzureBoundedRetry()
        new_retry.total = retry.total
        new_retry.connect = retry.connect
        new_retry.read = retry.read
        new_retry.backoff_factor = retry.backoff_factor
        new_retry.BACKOFF_MAX = retry.BACKOFF_MAX
        new_retry.status_forcelist = retry.status_forcelist
        new_retry.method_whitelist = retry.method_whitelist

        return new_retry

    def get_retry_after(self, response):
        retry_after = super().get_retry_after(response)
        if response.status != http.HTTPStatus.TOO_MANY_REQUESTS or retry_after <= _RETRY_TIME_LIMIT:
            return retry_after

        headers = {}
        for header in ['Retry-After',
                       'x-ms-ratelimit-remaining-subscription-reads',
                       'x-ms-ratelimit-remaining-subscription-writes',
                       'x-ms-ratelimit-remaining-tenant-reads',
                       'x-ms-ratelimit-remaining-tenant-writes',
                       'x-ms-ratelimit-remaining-subscription-resource-requests',
                       'x-ms-ratelimit-remaining-subscription-resource-entities-read',
                       'x-ms-ratelimit-remaining-tenant-resource-requests',
                       'x-ms-ratelimit-remaining-tenant-resource-entities-read']:
            value = response.getheader(header)
            if value is not None:
                headers[header] = value

        logger.warn("Azure request throttled: {}".format(headers))
        return _RETRY_TIME_LIMIT


class AzureGroups(object):
    def __init__(self, resource_groups, slow_scale_classes, client: AzureApi):
        self.resource_groups = resource_groups
        self.slow_scale_classes = slow_scale_classes
        self.client = client

    def get_all_groups(self, kube_nodes):

        groups = []
        if self.client:
            for resource_group in self.resource_groups:
                scale_sets_by_type = {}
                for scale_set in self.client.list_scale_sets(resource_group.name):
                    scale_sets_by_type.setdefault((scale_set.location, scale_set.instance_type), []).append(scale_set)
                for key, scale_sets in scale_sets_by_type.items():
                    location, instance_type = key
                    slow_scale = _get_azure_class(instance_type) in self.slow_scale_classes
                    groups.append(AzureVirtualScaleSet(location, resource_group.name, self.client, instance_type, slow_scale, scale_sets, kube_nodes))

        return groups


_CLASS_PAT = re.compile(r'\w+_(?P<class>[A-Z]+).+')


def _get_azure_class(type_):
    m = _CLASS_PAT.match(type_)
    return m.group('class')


_SCALE_SET_SIZE_LIMIT = 300


# Appears as an unbounded scale set. Currently, Azure Scale Sets have a limit of 300 hosts.
class AzureVirtualScaleSet(AutoScalingGroup):
    provider = 'azure'

    def __init__(self, region, resource_group, client: AzureApi, instance_type, slow_scale: bool, scale_sets: List[AzureScaleSet], kube_nodes):
        self.client = client
        self.instance_type = instance_type
        self.tags = {}
        self.name = 'virtual_scale_set_' + instance_type + '_' + region + '_' + resource_group
        self.scale_sets = dict((scale_set.name, scale_set) for scale_set in scale_sets)
        self.desired_capacity = sum(scale_set.capacity for scale_set in scale_sets)

        self.region = region
        self.resource_group = resource_group

        self.selectors = dict(self.tags)
        # HACK: for matching node selectors
        self.selectors['azure/type'] = self.instance_type
        self.selectors['azure/class'] = _get_azure_class(self.instance_type)
        self.slow_scale = slow_scale

        self.min_size = 0
        self.max_size = 10000
        self.is_spot = False

        self.vm_id_to_instance: MutableMapping[str, Tuple[str, AzureScaleSetInstance]] = {}
        self.instances = {}
        self.timeout_until = None
        self.timeout_reason = None
        self._global_priority = None
        self.no_schedule_taints = {}
        for scale_set in scale_sets:
            if scale_set.timeout_until is not None:
                if self.timeout_until is None or self.timeout_until < scale_set.timeout_until:
                    self.timeout_until = scale_set.timeout_until
                    self.timeout_reason = scale_set.name + ": " + scale_set.timeout_reason
            if scale_set.priority is not None:
                if self._global_priority is None:
                    self._global_priority = scale_set.priority
                else:
                    self._global_priority = min(scale_set.priority, self._global_priority)
            if not self.no_schedule_taints:
                self.no_schedule_taints = scale_set.no_schedule_taints

            if scale_set.capacity == 0:
                continue
            for instance in self.client.list_scale_set_instances(scale_set):
                self.vm_id_to_instance[instance.vm_id] = (scale_set.name, instance)
                self.instances[instance.vm_id] = AzureInstance(instance.vm_id, self.instance_type, instance.launch_time, self.tags)

        self.nodes = [node for node in kube_nodes if node.instance_id in self.vm_id_to_instance]
        self.unschedulable_nodes = [n for n in self.nodes if n.unschedulable]

        self._id = (self.region, self.name)

    def is_timed_out(self):
        if self.timeout_until and datetime.now(self.timeout_until.tzinfo) < self.timeout_until:
            logger.warn("{} is timed out until {} because {}".format(self._id, self.timeout_until, self.timeout_reason))
            return True
        return False

    @property
    def global_priority(self):
        if self._global_priority is None:
            return super().global_priority
        return self._global_priority

    def get_azure_instances(self):
        return self.instances.values()

    @property
    def instance_ids(self):
        return self.vm_id_to_instance.keys()

    def set_desired_capacity(self, new_desired_capacity):
        """
        sets the desired capacity of the underlying ASG directly.
        note that this is for internal control.
        for scaling purposes, please use scale() instead.
        """
        scale_out = new_desired_capacity - self.desired_capacity
        assert scale_out >= 0
        if scale_out == 0:
            return CompletedFuture(False)

        remaining_instances = self.client.get_remaining_instances(self.resource_group, self.instance_type)

        futures = []
        for scale_set in sorted(self.scale_sets.values(), key=lambda x: (x.priority, x.name)):
            if scale_set.capacity < _SCALE_SET_SIZE_LIMIT:
                if self.slow_scale:
                    new_group_capacity = scale_set.capacity + 1
                else:
                    new_group_capacity = min(_SCALE_SET_SIZE_LIMIT, scale_set.capacity + scale_out, scale_set.capacity + remaining_instances)
                if scale_set.provisioning_state == 'Updating':
                    logger.warn("Update of {} already in progress".format(scale_set.name))
                    continue
                if scale_set.provisioning_state == 'Failed':
                    logger.error("{} failed provisioning. Skipping it for scaling.".format(scale_set.name))
                    continue
                scale_out -= (new_group_capacity - scale_set.capacity)
                remaining_instances -= (new_group_capacity - scale_set.capacity)
                # Update our cached version
                self.scale_sets[scale_set.name].capacity = new_group_capacity
                futures.append(self.client.update_scale_set(scale_set, new_group_capacity))
                logger.info("Scaling Azure Scale Set {} to {}".format(scale_set.name, new_group_capacity))
            if scale_out == 0 or remaining_instances == 0:
                break

        if remaining_instances == 0:
            logger.warning("Out of quota for {}!".format(self.instance_type))

        if scale_out > 0:
            logger.error("Not enough scale sets to reach desired capacity {} for {}".format(new_desired_capacity, self))

        self.desired_capacity = new_desired_capacity - scale_out
        logger.info("ASG: {} new_desired_capacity: {}".format(self, new_desired_capacity))

        return TransformingFuture(True, AllCompletedFuture(futures))

    def terminate_instances(self, vm_ids):
        vm_ids = list(vm_ids)
        instances = {}
        for vm_id in vm_ids:
            scale_set_name, instance = self.vm_id_to_instance[vm_id]
            # Update our cached copy of the Scale Set
            self.scale_sets[scale_set_name].capacity -= 1
            instances.setdefault(scale_set_name, []).append(instance)
        logger.info('Terminated instances %s', vm_ids)

        futures = []
        for scale_set_name, scale_set_instances in instances.items():
            futures.append(self.client.terminate_scale_set_instances(self.scale_sets[scale_set_name], scale_set_instances))
        return AllCompletedFuture(futures)

    def scale_nodes_in(self, nodes):
        """
        scale down asg by terminating the given node.
        returns a future indicating when the request completes.
        """
        for node in nodes:
            self.nodes.remove(node)
        return self.terminate_instances(node.instance_id for node in nodes)

    def __str__(self):
        return 'AzureVirtualScaleSet({name}, {selectors_hash})'.format(name=self.name, selectors_hash=utils.selectors_to_hash(self.selectors))

    def __repr__(self):
        return str(self)


class AzureInstance(object):
    provider = 'azure'

    def __init__(self, instance_id, instance_type, launch_time, tags):
        self.id = instance_id
        self.instance_type = instance_type
        self.launch_time = launch_time
        self.tags = tags

    def __str__(self):
        return 'AzureInstance({}, {})'.format(self.id, self.instance_type)

    def __repr__(self):
        return str(self)