# (generated with --quick)

from typing import Any, Optional

Et: module
Sdk: Any

class AyxPlugin:
    __doc__: str
    alteryx_engine: Any
    current_group: None
    current_value: Optional[int]
    grouping_fields: Any
    grouping_fields_objects: None
    is_initialized: bool
    n_tool_id: Any
    output_anchor: Any
    output_anchor_mgr: Any
    output_field: None
    output_field_last: Any
    output_field_name: Any
    output_field_size: Optional[int]
    output_field_type: Any
    single_input: Optional[IncomingInterface]
    starting_value: Optional[int]
    xml_sort_info: Optional[str]
    def __init__(self, n_tool_id, alteryx_engine, output_anchor_mgr) -> None: ...
    def display_error_msg(self, msg_string) -> None: ...
    def pi_add_incoming_connection(self, str_type, str_name) -> IncomingInterface: ...
    def pi_add_outgoing_connection(self, str_name) -> bool: ...
    def pi_close(self, b_has_errors) -> None: ...
    def pi_init(self, str_xml) -> None: ...
    def pi_push_all_records(self, n_record_limit) -> bool: ...

class IncomingInterface:
    __doc__: str
    parent: Any
    record_copier: Any
    record_creator: Any
    def __init__(self, parent) -> None: ...
    def ii_close(self) -> None: ...
    def ii_init(self, record_info_in) -> bool: ...
    def ii_push_record(self, in_record) -> bool: ...
    def ii_update_progress(self, d_percent) -> None: ...
