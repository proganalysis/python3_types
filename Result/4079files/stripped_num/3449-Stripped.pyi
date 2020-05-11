# (generated with --quick)

from typing import Any, Tuple

BrainConfiguration: Any
ET: module
FileFinder: Any
LineNumberingParser: Any
ParserException: Any
PatternGraph: Any
PatternMatcher: Any
Sentence: Any
TemplateEvaluator: Any
TemplateGraph: Any
logging: module

class AIMLLoader(Any):
    aiml_parser: Any
    def __init__(self, aiml_parser) -> None: ...
    def load_file_contents(self, filename) -> Any: ...

class AIMLParser(object):
    _aiml_loader: AIMLLoader
    _filename: Any
    _num_categories: int
    _supress_warnings: Any
    _version: Any
    num_categories: Any
    pattern_matcher: Any
    pattern_parser: Any
    stop_on_invalid: Any
    supress_warnings: Any
    template_evaluator: Any
    template_parser: Any
    def __init__(self, supress_warnings = ..., stop_on_invalid = ...) -> None: ...
    def load_aiml(self, brain_configuration) -> None: ...
    def match_sentence(self, bot, clientid, sentence, parent_question, topic_pattern, that_pattern) -> Any: ...
    def parse_aiml(self, aiml_xml, filename) -> None: ...
    def parse_category(self, category_xml, topic_element = ..., add_to_graph = ...) -> Tuple[Any, Any, Any, Any]: ...
    def parse_from_file(self, filename) -> None: ...
    def parse_from_text(self, text) -> None: ...
    def parse_topic(self, topic_element) -> None: ...
    def parse_version(self, aiml) -> None: ...
