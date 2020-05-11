# (generated with --quick)

from typing import Any, Tuple

argparse: module
os: module
parser: argparse.ArgumentParser
reader: module
testopt: argparse.Namespace
time: module
torch: Any

def evalulate(model, data, vocab_dict) -> Any: ...
def get_stories(story_lines, with_answer = ...) -> Any: ...
def load_testdata(testfile, vocab_dict, with_answer = ...) -> Any: ...
def main() -> None: ...
def vectorize_stories(stories, vocab) -> Tuple[list, list, Any, list]: ...
