# (generated with --quick)

from typing import Any

Address: Any
Calldata: Any
DSProxy: Any
DSProxyCache: Any
DSProxyFactory: Any
LogCreated: Any
Web3: Any
other_address: Any
our_address: Any
proxy: Any
proxy_cache: Any
proxy_factory: Any
pytest: Any
web3: Any

class TestProxy:
    __doc__: str
    def test_call(self, proxy) -> None: ...
    def test_call_at(self, proxy) -> None: ...
    def test_execute(self, proxy) -> None: ...
    def test_execute_at(self, proxy) -> None: ...

class TestProxyCache:
    __doc__: str
    def test_read(self, proxy_cache) -> None: ...
    def test_write(self, proxy_cache) -> None: ...
    def test_write_invalid(self, proxy_cache) -> None: ...

class TestProxyFactory:
    __doc__: str
    def test_build(self, proxy_factory) -> None: ...
    def test_build_for(self, proxy_factory, other_address) -> None: ...
    def test_cache(self, proxy_factory, other_address) -> None: ...
    def test_past_build(self, proxy_factory, our_address) -> None: ...
