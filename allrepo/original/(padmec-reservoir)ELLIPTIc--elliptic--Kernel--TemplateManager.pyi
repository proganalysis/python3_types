# (generated with --quick)

import jinja2.environment
import jinja2.loaders
from typing import Type

Environment: Type[jinja2.environment.Environment]
PackageLoader: Type[jinja2.loaders.PackageLoader]
Template: Type[jinja2.environment.Template]

class TemplateManagerBase:
    __doc__: str
    jinja2_env: jinja2.environment.Environment
    def __init__(self, package: str, templates_folder: str) -> None: ...
    def get_template(self, template_file: str) -> jinja2.environment.Template: ...
    def render(self, template_file: str, **kwargs: str) -> str: ...
