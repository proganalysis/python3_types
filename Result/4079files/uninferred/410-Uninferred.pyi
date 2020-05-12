from .prop_codes import *
from .primitive import *
from .standard import *
from typing import Any

def prop_map(code: int) -> Any: ...

class PropBase:
    prop_code: Any = ...
    prop_data_class: Any = ...
    @classmethod
    def build_header(cls): ...
    @classmethod
    def parse(cls: Any, connection: Connection) -> Any: ...
    @classmethod
    def to_python(cls, ctype_object: Any, *args: Any, **kwargs: Any): ...
    @classmethod
    def from_python(cls, value: Any): ...

class PropName(PropBase):
    prop_code: Any = ...
    prop_data_class: Any = ...

class PropCacheMode(PropBase):
    prop_code: Any = ...
    prop_data_class: Any = ...

class PropCacheAtomicityMode(PropBase):
    prop_code: Any = ...
    prop_data_class: Any = ...

class PropBackupsNumber(PropBase):
    prop_code: Any = ...
    prop_data_class: Any = ...

class PropWriteSynchronizationMode(PropBase):
    prop_code: Any = ...
    prop_data_class: Any = ...

class PropCopyOnRead(PropBase):
    prop_code: Any = ...
    prop_data_class: Any = ...

class PropReadFromBackup(PropBase):
    prop_code: Any = ...
    prop_data_class: Any = ...

class PropDataRegionName(PropBase):
    prop_code: Any = ...
    prop_data_class: Any = ...

class PropIsOnheapCacheEnabled(PropBase):
    prop_code: Any = ...
    prop_data_class: Any = ...

class PropQueryEntities(PropBase):
    prop_code: Any = ...
    prop_data_class: Any = ...

class PropQueryParallelism(PropBase):
    prop_code: Any = ...
    prop_data_class: Any = ...

class PropQueryDetailMetricSize(PropBase):
    prop_code: Any = ...
    prop_data_class: Any = ...

class PropSQLSchema(PropBase):
    prop_code: Any = ...
    prop_data_class: Any = ...

class PropSQLIndexInlineMaxSize(PropBase):
    prop_code: Any = ...
    prop_data_class: Any = ...

class PropSqlEscapeAll(PropBase):
    prop_code: Any = ...
    prop_data_class: Any = ...

class PropMaxQueryIterators(PropBase):
    prop_code: Any = ...
    prop_data_class: Any = ...

class PropRebalanceMode(PropBase):
    prop_code: Any = ...
    prop_data_class: Any = ...

class PropRebalanceDelay(PropBase):
    prop_code: Any = ...
    prop_data_class: Any = ...

class PropRebalanceTimeout(PropBase):
    prop_code: Any = ...
    prop_data_class: Any = ...

class PropRebalanceBatchSize(PropBase):
    prop_code: Any = ...
    prop_data_class: Any = ...

class PropRebalanceBatchesPrefetchCount(PropBase):
    prop_code: Any = ...
    prop_data_class: Any = ...

class PropRebalanceOrder(PropBase):
    prop_code: Any = ...
    prop_data_class: Any = ...

class PropRebalanceThrottle(PropBase):
    prop_code: Any = ...
    prop_data_class: Any = ...

class PropGroupName(PropBase):
    prop_code: Any = ...
    prop_data_class: Any = ...

class PropCacheKeyConfiguration(PropBase):
    prop_code: Any = ...
    prop_data_class: Any = ...

class PropDefaultLockTimeout(PropBase):
    prop_code: Any = ...
    prop_data_class: Any = ...

class PropMaxConcurrentAsyncOperation(PropBase):
    prop_code: Any = ...
    prop_data_class: Any = ...

class PropPartitionLossPolicy(PropBase):
    prop_code: Any = ...
    prop_data_class: Any = ...

class PropEagerTTL(PropBase):
    prop_code: Any = ...
    prop_data_class: Any = ...

class PropStatisticsEnabled(PropBase):
    prop_code: Any = ...
    prop_data_class: Any = ...

class AnyProperty(PropBase):
    @classmethod
    def from_python(cls, value: Any) -> None: ...
    @classmethod
    def to_python(cls, ctype_object: Any, *args: Any, **kwargs: Any): ...
