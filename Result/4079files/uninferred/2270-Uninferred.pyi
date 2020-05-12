from behave import *
from behave.runner import Context as Context
from grakn.client import Graph as Graph
from nose.tools import eq_ as eq_
from typing import Any

def step_impl(context: Context) -> Any: ...
