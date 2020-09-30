import logging
import math
import time
from functools import wraps


def retry_on_exception(tries: int = 6, delay: int = 1, backoff: int = 2, max_delay: int = 32):
    """为重新尝试失败而实现指数回溯的装饰者。

    :param tries: 在失败之前执行包装功能的最大次数
    :param delay: 在第一次重试之前的几秒钟内延迟时间
    :param backoff: 通过每次重试来扩展初始延迟的乘数
    :param max_delay: 在重试之间等待的时间为秒
    :return:
    """
    tries = math.floor(tries)
    if tries < 1:
        raise ValueError('"tries" must be greater than or equal to 1.')
    if delay < 0:
        raise ValueError('"delay" must be greater than or equal to 0.')
    if backoff < 1:
        raise ValueError('"backoff" must be greater than or equal to 1.')
    if max_delay < delay:
        raise ValueError('"max_delay" must be greater than or equal to delay.')

    def decorated_function_with_retry(func):
        @wraps(func)
        def function_to_retry(*args, **kwargs):
            local_tries, local_delay = tries, delay
            while local_tries > 1:
                try:
                    return func(*args, **kwargs)
                except Exception as e:
                    if local_delay > max_delay:
                        local_delay = max_delay
                    logging.exception('%s: Retrying in %d seconds...' %
                                      (str(e), local_delay))
                    time.sleep(local_delay)
                    local_tries -= 1
                    local_delay *= backoff
            return func(*args, **kwargs)

        return function_to_retry

    return decorated_function_with_retry
