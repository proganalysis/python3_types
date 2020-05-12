# (generated with --quick)

import bucket_throttling
import datetime
from typing import Any, List, Type

BucketList = List[bucket_throttling.ThrottlingBucket]
RuleList = List[bucket_throttling.ThrottlingRule]

ThrottlingBucket: Type[bucket_throttling.ThrottlingBucket]
ThrottlingOptions: Type[bucket_throttling.ThrottlingOptions]
ThrottlingRule: Type[bucket_throttling.ThrottlingRule]
timedelta: Type[datetime.timedelta]

def check_throttle(buckets) -> Any: ...
def commit_request(buckets) -> None: ...
def get_buckets(rules, arguments_bundle, options = ...) -> List[bucket_throttling.ThrottlingBucket]: ...
