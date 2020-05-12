# (generated with --quick)

import __future__
from typing import Any

EQ_REFL: str
EQ_SYM: str
FLAGS: Any
HOLLIGHT_TACTICS_TEXTPB_PATH: Any
MOCK_PREMISE_SET: Any
MOCK_THEOREM: Any
MOCK_WRAPPER: MockProofAssistantWrapper
PREDICTIONS_MODEL_PREFIX: Any
absolute_import: __future__._Feature
action_generator: Any
deephol_pb2: Any
division: __future__._Feature
embedding_store: Any
flags: Any
holparam_predictor: Any
parameterized: Any
print_function: __future__._Feature
proof_assistant_pb2: Any
proof_search_tree: Any
prover_util: Any
test_util: Any
text_format: Any
tf: Any
theorem_fingerprint: Any

class ActionGeneratorTest(Any):
    node: Any
    test_action_generator_theorem_list_parameter_tactic: Any
    test_compute_parameter_string: Any
    tree: Any
    def setUp(self) -> None: ...
    @classmethod
    def setUpClass(cls) -> None: ...
    def test_action_generator_hol_light_tactics_sanity_check(self) -> None: ...
    def test_action_generator_no_parameter_tactic(self) -> None: ...
    def test_action_generator_theorem_parameter_tactic(self) -> None: ...
    def test_action_generator_unknown_parameter_tactic(self) -> None: ...
    def test_compute_parameter_string_unknown(self) -> None: ...

class MockActionGenerator(Any):
    suggestions: Any
    def __init__(self, suggestions) -> None: ...
    def step(self, goal, premise_set) -> Any: ...

class MockProofAssistantWrapper(object):
    def ApplyTactic(self, request) -> Any: ...

def load_tactics(filename) -> Any: ...
def mock_generator(*tactic_scores) -> MockActionGenerator: ...
