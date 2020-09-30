# (generated with --quick)

import asyncio.events
from typing import Any, Type
import unittest.case

TestCase: Type[unittest.case.TestCase]
aioredis: Any
asyncio: module

class BaseTestCase(unittest.case.TestCase):
    db: Any
    loop: asyncio.events.AbstractEventLoop
