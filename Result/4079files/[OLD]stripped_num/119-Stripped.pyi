# (generated with --quick)

from typing import Any, Dict, List, Tuple

CheckboxSelectMultiple: Any
ChoiceField: Any
Field: Any
RadioSelect: Any
Select: Any
TextInput: Any
logger: logging.Logger
logging: module

class CheckboxConditionalSelectMultiple(ConditionalSelectMixin, Any):
    __doc__: str

class ConditionalField(object):
    @classmethod
    def dropdown(cls, choice) -> Any: ...
    @classmethod
    def textinfo(cls, choice) -> Any: ...

class ConditionalGenerator(object):
    __doc__: str
    choice: Any
    dropdown_var: str
    querydict: Any
    text_var: str
    def context_from_conditional_type(self) -> Dict[str, Any]: ...
    def context_from_field(self, field) -> Any: ...
    @classmethod
    def generate_context(cls, choice, querydict) -> Any: ...

class ConditionalSelect(ConditionalSelectMixin, Any):
    __doc__: str

class ConditionalSelectMixin:
    __doc__: str
    option_template_name: str
    querydict: Any
    def create_option(self, *args, **kwargs) -> Any: ...
    def value_from_datadict(self, data, files, name) -> Any: ...

class RadioConditionalSelect(ConditionalSelectMixin, Any):
    __doc__: str

def conditional_field_from_choice(choice) -> Any: ...
def conditional_id(choice) -> str: ...
def options_as_choices(data) -> List[Tuple[Any, Any]]: ...
