# (generated with --quick)

from typing import Any, Dict, List, Set, TextIO, Union

BUCKET: str
CLASS_LIST: List[str]
EXP_NAME: str
all_labels: List[List[str]]
boto3: Any
bucket_region: Any
copy_source: Dict[str, str]
dataset_size: int
f: TextIO
img: str
img_examples: List[str]
img_id: int
img_path: str
ims: Dict[str, Union[List[str], Set[str]]]
input_data_paths: List[str]
itertools: module
json: module
json_body: Dict[str, List[Dict[str, str]]]
key: str
np: module
num_classes: int
region: Any
s3: Any
train_data_paths: List[str]
train_test_split_index: int
validation_data_paths: List[str]

def make_template(test_template = ..., save_fname = ...) -> None: ...
