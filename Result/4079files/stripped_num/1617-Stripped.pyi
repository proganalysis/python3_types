# (generated with --quick)

from typing import Any, Generator

AbstractBlockchainInstanceProvider: Any
BlockchainObject: Any
BlockchainObjects: Any
ProposalDoesNotExistException: Any
log: logging.Logger
logging: module
parse_time: Any

class Proposal(Any, Any):
    __doc__: str
    expiration: Any
    is_in_review: bool
    proposed_operations: Generator[nothing, Any, None]
    proposer: Any
    review_period: Any
    def __init__(self, data, *args, **kwargs) -> None: ...
    def refresh(self) -> None: ...

class Proposals(Any, Any):
    __doc__: str
    identifier: Any
    def __init__(self, account, *args, **kwargs) -> None: ...
    def refresh(self, *args, **kwargs) -> None: ...
