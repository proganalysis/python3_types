# (generated with --quick)

import bucket_throttling
import datetime
from typing import List, Optional, Type

BucketList = List[bucket_throttling.ThrottlingBucket]
RuleList = List[bucket_throttling.ThrottlingRule]

ThrottlingBucket: Type[bucket_throttling.ThrottlingBucket]
ThrottlingOptions: Type[bucket_throttling.ThrottlingOptions]
ThrottlingRule: Type[bucket_throttling.ThrottlingRule]
timedelta: Type[datetime.timedelta]

def check_throttle(buckets: List[bucket_throttling.ThrottlingBucket]) -> datetime.timedelta: ...
def commit_request(buckets: List[bucket_throttling.ThrottlingBucket]) -> None: ...
def get_buckets(rules: List[bucket_throttling.ThrottlingRule], arguments_bundle: dict, options: Optional[bucket_throttling.ThrottlingOptions] = ...) -> List[bucket_throttling.ThrottlingBucket]: ...
