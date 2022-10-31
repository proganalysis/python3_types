from typing import Any

class BotBuilder:
    slotJConverter: Any = ...
    intentConverter: Any = ...
    botJConverter: Any = ...
    output_dir: Any = ...
    lambda_arn_prefix: Any = ...
    client: Any = ...
    def __init__(self, workbook: Any, output_dir: Any, lambda_arn_prefix: Any) -> None: ...
    def __build_lex_component(self, name: str, func: Any) -> Any: ...
    @staticmethod
    def __delete_lex_component(name: str, func: Any) -> Any: ...
    def deploy_bot(self): ...
    def generate_cloudformation_resources(self) -> None: ...
    def undeploy_bot(self) -> None: ...