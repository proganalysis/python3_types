# -*- coding: utf-8 -*-
# Copyright (c) 2016-present, CloudZero, Inc. All rights reserved.
# Licensed under the BSD-style license. See LICENSE file in the project root for full license information.

from datetime import datetime, timezone

from botocore.exceptions import ClientError

import lambda_tools
from reactor.aws.provider import Provider
from reactor.database.models.dynamodb import common

logger = lambda_tools.setup_logging('reactor')


class CZReactorMetrics(common.CZReactorModel):
    _TABLE_BASENAME = 'cz_reactor_metrics'

    _TABLE_DEFINITION = {
        'KeySchema': [{'AttributeName': 'name', 'KeyType': 'HASH'},
                      {'AttributeName': 'range', 'KeyType': 'RANGE'}],
        'AttributeDefinitions': [{'AttributeName': 'name', 'AttributeType': 'S'},
                                 {'AttributeName': 'range', 'AttributeType': 'S'}],
        'ProvisionedThroughput': {'ReadCapacityUnits': 1, 'WriteCapacityUnits': 1}
    }

    def __init__(self, namespace: str = None, aws: Provider = None):
        """Instantiate a CZReactorMetric for this namespace.

        Args:
            namespace (str): A human-readable identifier for the current Reactor installation in AWS.
                             Distinct from Reactor ID, which is a UUID shared with Core.
            aws (Provider): session access to AWS
        """
        super().__init__(self._TABLE_BASENAME, namespace, aws)

    def get(self, name, range_key):
        """Get metrics for given hash and range key.

        Args:
            name (str): Name of the metric to retrieve
            range_key (str): Range key for the metric (?)

        Ret:
            metric (dict): metric details
        """
        try:
            metric = self.table.get_item(Key={
                'name': name,
                'range': range_key,
            }).get('Item')

            return metric if metric else {}
        except ClientError as err:
            logger.warning(f'ClientError {err} while trying to get metric named {name} with range key {range_key}')
            return {}

    def write_metric(self, event_count, metric_name, env_id='root'):
        """
        Records a simple metric record to dynamodb so we can keep track of activity over time.

        Args:
            event_count (int): The number of occurrences of the event to record with this update
            metric_name (str): The unique name of the metric being recorded.
            env_id (str): The environment ID associated with the metric record.  Defaults to 'root'.

        Returns:
            The latest value of the recorded metric (dict)
        """
        current_hour = datetime.now(timezone.utc).strftime("%Y/%m/%d:%H")
        hash_key = "{}-{}".format(metric_name, env_id)

        try:
            result = self.table.update_item(Key={
                'name': hash_key,
                'range': str(current_hour),
            }, AttributeUpdates={
                'count': {
                    'Action': 'ADD',
                    'Value': int(event_count),
                },
                'last_updated': {
                    'Action': 'PUT',
                    'Value': datetime.now(timezone.utc).isoformat()
                }
            }, ReturnValues='ALL_NEW')
        except ClientError as err:
            if "ProvisionedThroughputExceededException" in str(err):
                logger.warning('Mostly harmless: exceeded provisioned throughput updating metrics')
                return None
            else:
                raise

        return result.get('Attributes')
