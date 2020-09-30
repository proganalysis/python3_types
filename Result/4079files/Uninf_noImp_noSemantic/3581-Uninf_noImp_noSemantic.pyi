from typing import Any

BUCKET: str
EXP_NAME: str
region: Any
s3: Any
bucket_region: Any
all_labels: Any
ims: Any
num_classes: Any
copy_source: Any
input_data_paths: Any
dataset_size: Any
train_test_split_index: Any
train_data_paths: Any
validation_data_paths: Any
CLASS_LIST: Any
json_body: Any
img_examples: Any

def make_template(test_template: bool = ..., save_fname: str = ...) -> None: ...
