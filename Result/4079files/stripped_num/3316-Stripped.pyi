# (generated with --quick)

import converter.BotJsonConverter
import converter.IntentConverter
import converter.SlotJsonConverter
from typing import Any, Type

BotJsonConverter: Type[converter.BotJsonConverter.BotJsonConverter]
IntentConverter: Type[converter.IntentConverter.IntentConverter]
SlotJsonConverter: Type[converter.SlotJsonConverter.SlotJsonConverter]
bot_builder1: BotBuilder
boto3: Any
json: module
os: module
time: module

class BotBuilder:
    botJConverter: converter.BotJsonConverter.BotJsonConverter
    client: Any
    intentConverter: converter.IntentConverter.IntentConverter
    lambda_arn_prefix: Any
    output_dir: Any
    slotJConverter: converter.SlotJsonConverter.SlotJsonConverter
    def _BotBuilder__build_lex_component(self, name, func) -> None: ...
    @staticmethod
    def _BotBuilder__delete_lex_component(name, func) -> None: ...
    def __init__(self, workbook, output_dir, lambda_arn_prefix) -> None: ...
    def deploy_bot(self) -> None: ...
    def generate_cloudformation_resources(self) -> None: ...
    def undeploy_bot(self) -> None: ...
