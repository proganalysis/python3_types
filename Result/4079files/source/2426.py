import unittest
import time

from bucket_throttling.utils import *
from bucket_throttling import ThrottlingOptions


def try_request(rules: list, options, request_arguments: dict, delay_after: float, expected_result: bool):
    buckets = get_buckets(rules, request_arguments, options)
    timeout = check_throttle(buckets)
    if not timeout:
        commit_request(buckets)
    if not expected_result and not timeout:
        raise AssertionError('Must throttle, but passed')
    elif expected_result and timeout:
        raise AssertionError('Must pass, but throttled for %s' % str(timeout))
    time.sleep(delay_after)


class MultipleUserTest(unittest.TestCase):
    TEST_RULES = [
        ThrottlingRule(max_requests=1, interval=timedelta(seconds=1)),
        ThrottlingRule(max_requests=2, interval=timedelta(seconds=5)),
    ]

    TEST_OPTIONS = ThrottlingOptions(verbose_mode=True, periods_to_overtake=0)

    def __init__(self, methodName='runTest'):
        super().__init__(methodName)

    @staticmethod
    def user_test(user_id: int, rules, options):
        try_request(rules, options, dict(path='path1', user_id=user_id), 0.2, True)
        try_request(rules, options, dict(path='path1', user_id=user_id), 1, False)
        try_request(rules, options, dict(path='path1', user_id=user_id), 0.1, True)
        try_request(rules, options, dict(path='path1', user_id=user_id), 0.1, False)

        try_request(rules, options, dict(path='path2', user_id=user_id), 0.1, True)
        try_request(rules, options, dict(path='path2', user_id=user_id), 1, False)
        try_request(rules, options, dict(path='path2', user_id=user_id), 0.1, True)
        try_request(rules, options, dict(path='path2', user_id=user_id), 0.1, False)

    def test_users(self):
        self.user_test(1, self.TEST_RULES, self.TEST_OPTIONS)
        self.user_test(2, self.TEST_RULES, self.TEST_OPTIONS)


class BurstTest(unittest.TestCase):
    TEST_RULES = [
        ThrottlingRule(max_requests=30, interval=timedelta(seconds=3)),
    ]

    TEST_OPTIONS = ThrottlingOptions(verbose_mode=True, periods_to_overtake=1)  # , redis_options={'port': 6363}

    def __init__(self, methodName='runTest'):
        super().__init__(methodName)

    @staticmethod
    def burst_test(user_id: int, rules, options):
        for i in range(15):
            try_request(rules, options, dict(path='path3', user_id=user_id), 0.01, True)
        time.sleep(3)
        for i in range(45):
            try_request(rules, options, dict(path='path3', user_id=user_id), 0.01, True)
        try_request(rules, options, dict(path='path3', user_id=user_id), 0.01, False)
        time.sleep(3)

    def test_burst(self):
        self.burst_test(1, self.TEST_RULES, self.TEST_OPTIONS)
        self.burst_test(1, self.TEST_RULES, self.TEST_OPTIONS)


if __name__ == "__main__":
    unittest.main()
