from typing import Any

platform: str
dataflow_tf_data_validation_op: Any
dataflow_tf_transform_op: Any
tf_train_op: Any
dataflow_tf_model_analyze_op: Any
dataflow_tf_predict_op: Any
confusion_matrix_op: Any
roc_op: Any
kubeflow_deploy_op: Any

def taxi_cab_classification(output: Any, project: Any, column_names: str = ..., key_columns: str = ..., train: str = ..., evaluation: str = ..., mode: str = ..., preprocess_module: str = ..., learning_rate: float = ..., hidden_layer_size: str = ..., steps: int = ..., analyze_slice_column: str = ...) -> None: ...
