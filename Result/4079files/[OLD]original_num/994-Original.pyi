# (generated with --quick)

from typing import Any

BayesianDecoder: Any
BayesianEncoder: Any
np: module
seq2seq: Any
tf: Any

class Model:
    config: Any
    decoder: Any
    encoder: Any
    evidence_loss: Any
    gen_loss: Any
    initial_state: Any
    latent_loss: Any
    loss: Any
    probs: Any
    psi: Any
    targets: Any
    train_op: Any
    def __init__(self, config, infer = ...) -> None: ...
    def infer_ast(self, sess, psi, tokens) -> Any: ...
    def infer_psi(self, sess, evidences) -> Any: ...
