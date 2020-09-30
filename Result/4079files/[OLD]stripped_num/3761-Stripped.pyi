# (generated with --quick)

import pairwise_models.emb_extra_layer
import pairwise_models.model
import pairwise_models.shared_w_trans_layer
import pairwise_models.simple
import pairwise_models.smt
from typing import Dict, Type

EmbExtraLayer: Type[pairwise_models.emb_extra_layer.EmbExtraLayer]
Model: Type[pairwise_models.model.Model]
SMTModel: Type[pairwise_models.smt.SMTModel]
SharedWeightTransLayer: Type[pairwise_models.shared_w_trans_layer.SharedWeightTransLayer]
SimpleModel: Type[pairwise_models.simple.SimpleModel]
json: module
re: module

def get_custom_models() -> Dict[str, Type[pairwise_models.simple.SimpleModel]]: ...
def restore_definition(filename) -> pairwise_models.simple.SimpleModel: ...
