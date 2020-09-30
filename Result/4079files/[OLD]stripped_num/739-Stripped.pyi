# (generated with --quick)

from typing import Any

logging: module
os: module
shutil: module
tf: Any
util: Any

class TensorflowGraph(Any):
    Biases: list
    H: list
    Weights: list
    activator: Any
    batch_norm: Any
    checkpoint_dir: Any
    cnn_size: Any
    cnn_stride: int
    complexity: Any
    dropout: bool
    dropout_rate: Any
    enable_log: Any
    features: str
    initializer: Any
    is_training: None
    log_weight_image_num: int
    name: str
    pix_per_input: Any
    receptive_fields: Any
    save_images: Any
    save_images_num: Any
    save_meta_data: Any
    save_weights: Any
    saver: Any
    sess: Any
    summary_op: Any
    test_writer: Any
    tf_log_dir: Any
    train_writer: Any
    weight_dev: Any
    def __init__(self, flags) -> None: ...
    def build_activator(self, input_tensor, features, activator = ..., leaky_relu_alpha = ..., base_name = ...) -> Any: ...
    def build_conv(self, name, input_tensor, cnn_size, input_feature_num, output_feature_num, use_bias = ..., activator = ..., use_batch_norm = ..., dropout_rate = ...) -> Any: ...
    def build_depthwise_separable_conv(self, name, input_tensor, cnn_size, input_feature_num, output_feature_num, use_bias = ..., activator = ..., use_batch_norm = ..., dropout_rate = ...) -> Any: ...
    def build_pixel_shuffler_layer(self, name, h, scale, input_filters, output_filters, activator = ..., depthwise_separable = ...) -> None: ...
    def build_summary_saver(self, with_saver = ...) -> None: ...
    def build_transposed_conv(self, name, input_tensor, scale, channels) -> None: ...
    def conv2d(self, input_tensor, w, stride, bias = ..., use_batch_norm = ..., name = ...) -> Any: ...
    def copy_log_to_archive(self, archive_name) -> None: ...
    def depthwise_separable_conv2d(self, input_tensor, w, stride, channel_multiplier = ..., bias = ..., use_batch_norm = ..., name = ...) -> Any: ...
    def init_all_variables(self) -> None: ...
    def init_session(self, device_id = ...) -> None: ...
    def load_model(self, name = ..., trial = ..., output_log = ...) -> None: ...
    def save_model(self, name = ..., trial = ..., output_log = ...) -> None: ...
