# (generated with --quick)

import bucket_throttling
import datetime
from typing import Any, List, Type
import unittest.case

BucketList = List[bucket_throttling.ThrottlingBucket]
RuleList = List[bucket_throttling.ThrottlingRule]

ThrottlingBucket: Type[bucket_throttling.ThrottlingBucket]
ThrottlingOptions: Type[bucket_throttling.ThrottlingOptions]
ThrottlingRule: Type[bucket_throttling.ThrottlingRule]
time: module
timedelta: Type[datetime.timedelta]
unittest: module

class BurstTest(unittest.case.TestCase):
    TEST_OPTIONS: bucket_throttling.ThrottlingOptions
    TEST_RULES: List[bucket_throttling.ThrottlingRule]
    def __init__(self, methodName = ...) -> None: ...
    @staticmethod
    def burst_test(user_id, rules, options) -> None: ...
    def test_burst(self) -> None: ...

class MultipleUserTest(unittest.case.TestCase):
    TEST_OPTIONS: bucket_throttling.ThrottlingOptions
    TEST_RULES: List[bucket_throttling.ThrottlingRule]
    def __init__(self, methodName = ...) -> None: ...
    def test_users(self) -> None: ...
    @staticmethod
    def user_test(user_id, rules, options) -> None: ...

def check_throttle(buckets) -> Any: ...
def commit_request(buckets) -> None: ...
def get_buckets(rules, arguments_bundle, options = ...) -> List[bucket_throttling.ThrottlingBucket]: ...
def try_request(rules, options, request_arguments, delay_after, expected_result) -> None: ...
