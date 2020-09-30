# (generated with --quick)

import __future__
from typing import Any

AttentionDecoderCell: Any
Bidirectional: Any
Dense: Any
Dropout: Any
Input: Any
LSTMCell: Any
LSTMDecoderCell: Any
Model: Any
RecurrentSequential: Any
Sequential: Any
TimeDistributed: Any
absolute_import: __future__._Feature

def AttentionSeq2Seq(output_dim, output_length, batch_input_shape = ..., batch_size = ..., input_shape = ..., input_length = ..., input_dim = ..., hidden_dim = ..., depth = ..., bidirectional = ..., unroll = ..., stateful = ..., dropout = ...) -> Any: ...
def Seq2Seq(output_dim, output_length, batch_input_shape = ..., input_shape = ..., batch_size = ..., input_dim = ..., input_length = ..., hidden_dim = ..., depth = ..., broadcast_state = ..., unroll = ..., stateful = ..., inner_broadcast_state = ..., teacher_force = ..., peek = ..., dropout = ...) -> Any: ...
def SimpleSeq2Seq(output_dim, output_length, hidden_dim = ..., input_shape = ..., batch_size = ..., batch_input_shape = ..., input_dim = ..., input_length = ..., depth = ..., dropout = ..., unroll = ..., stateful = ...) -> Any: ...
