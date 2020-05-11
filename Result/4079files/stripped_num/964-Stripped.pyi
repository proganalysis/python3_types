# (generated with --quick)

import flask.globals
import sdconfig
from typing import Any

IntegrityError: Any
Journalist: Any
Reply: Any
Source: Any
Submission: Any
argparse: module
args: argparse.Namespace
config: sdconfig.SDConfig
current_app: flask.globals._FlaskLocalProxy
datetime: module
db: Any
journalist_app: module
os: module
parser: argparse.ArgumentParser

def add_test_user(username, password, otp_secret, is_admin = ...) -> None: ...
def create_source_and_submissions(num_submissions = ..., num_replies = ...) -> None: ...
def main(staging = ...) -> None: ...
