# (generated with --quick)

from typing import Any, Dict, List, Tuple, Type

BOOLEAN_KEYS: Tuple[str, str, str, str]
BaseEntity: Any
Comment: Any
DATETIME_KEYS: Tuple[str]
DiasporaComment: Any
DiasporaContact: Any
DiasporaImage: Any
DiasporaLike: Any
DiasporaPost: Any
DiasporaProfile: Any
DiasporaRelayableMixin: Any
DiasporaReshare: Any
DiasporaRetraction: Any
Follow: Any
INTEGER_KEYS: Tuple[str, str]
MAPPINGS: Dict[str, Any]
Post: Any
Profile: Any
Reaction: Any
ReceiverVariant: Any
Retraction: Any
RsaKey: Any
Share: Any
TAGS: List[str]
UserType: Any
datetime: Type[datetime.datetime]
etree: Any
get_element_child_info: Any
logger: logging.Logger
logging: module
retrieve_and_parse_profile: Any

def check_sender_and_entity_handle_match(sender_handle, entity_handle) -> bool: ...
def element_to_objects(element, sender, sender_key_fetcher = ..., user = ...) -> list: ...
def get_outbound_entity(entity, private_key) -> Any: ...
def message_to_objects(message, sender, sender_key_fetcher = ..., user = ...) -> list: ...
def transform_attributes(attrs, cls) -> dict: ...
def xml_children_as_dict(node) -> dict: ...
