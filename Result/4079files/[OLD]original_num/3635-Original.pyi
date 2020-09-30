# (generated with --quick)

from typing import Any, Tuple

ArrayType: Any
DeepImageFeaturizer: Any
DeepImagePredictor: Any
ImageSchema: Any
LogisticRegression: Any
MulticlassClassificationEvaluator: Any
Pipeline: Any
StringType: Any
udf: Any

class DL:
    @staticmethod
    def evaluate_image_classifier(df, model) -> Any: ...
    @staticmethod
    def image_classifier_lr(df, input_col = ..., output_col = ..., model_name = ...) -> Tuple[Any, Any]: ...
    @staticmethod
    def image_predictor(path, input_col = ..., output_col = ..., model_name = ..., decode_predictions = ..., topK = ...) -> Any: ...
