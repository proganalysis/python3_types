# (generated with --quick)

import bucket_throttling
import datetime
from typing import List, Optional, Type
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
    def burst_test(user_id: int, rules, options) -> None: ...
    def test_burst(self) -> None: ...

class MultipleUserTest(unittest.case.TestCase):
    TEST_OPTIONS: bucket_throttling.ThrottlingOptions
    TEST_RULES: List[bucket_throttling.ThrottlingRule]
    def __init__(self, methodName = ...) -> None: ...
    def test_users(self) -> None: ...
    @staticmethod
    def user_test(user_id: int, rules, options) -> None: ...

def check_throttle(buckets: List[bucket_throttling.ThrottlingBucket]) -> datetime.timedelta: ...
def commit_request(buckets: List[bucket_throttling.ThrottlingBucket]) -> None: ...
def get_buckets(rules: List[bucket_throttling.ThrottlingRule], arguments_bundle: dict, options: Optional[bucket_throttling.ThrottlingOptions] = ...) -> List[bucket_throttling.ThrottlingBucket]: ...
def try_request(rules: list, options, request_arguments: dict, delay_after: float, expected_result: bool) -> None: ...
