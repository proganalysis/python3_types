# (generated with --quick)

from typing import Any, List

StdSim: Any
argparse: module
cmd2: Any
mock: module
os: module
pytest: Any
random: module
re: module
run_cmd: Any
sys: module
tempfile: module
test_parse_transcript_expected: Any
test_transcript: Any
transcript: Any
verify_help_text: Any

class CmdLineApp(Any):
    MUMBLES: List[str]
    MUMBLE_FIRST: List[str]
    MUMBLE_LAST: List[str]
    do_mumble: Any
    do_orate: Any
    do_say: Any
    do_speak: Any
    feedback_to_output: Any
    intro: str
    maxrepeats: int
    mumble_parser: argparse.ArgumentParser
    speak_parser: argparse.ArgumentParser
    stdout: Any
    def __init__(self, *args, **kwargs) -> None: ...
    def do_nothing(self, statement) -> None: ...

def test_commands_at_invocation() -> None: ...
def test_generate_transcript_stop(capsys) -> None: ...
def test_history_transcript() -> None: ...
def test_history_transcript_bad_filename() -> None: ...
def test_run_script_record_transcript(base_app, request) -> None: ...
def test_transcript_failure(request, capsys) -> None: ...
def test_transcript_no_file(request, capsys) -> None: ...
