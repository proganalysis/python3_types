# (generated with --quick)

import __future__
from typing import Any, Tuple, Type

SOURCE_URL: str
absolute_import: __future__._Feature
base: Any
cv2: Any
division: __future__._Feature
dtypes: Any
gfile: Any
gzip: module
numpy: module
print_function: __future__._Feature
random_seed: Any
xrange: Type[range]

class DataSet(object):
    _epochs_completed: int
    _images: Any
    _index_in_epoch: Any
    _labels: Any
    _num_examples: Any
    epochs_completed: Any
    images: Any
    labels: Any
    num_examples: Any
    one_hot: Any
    def __init__(self, images, labels, fake_data = ..., one_hot = ..., dtype = ..., reshape = ..., seed = ...) -> None: ...
    def next_batch(self, batch_size, fake_data = ..., shuffle = ...) -> Tuple[Any, Any]: ...

def _read32(bytestream) -> Any: ...
def dense_to_one_hot(labels_dense, num_classes) -> Any: ...
def extract_images(f) -> Any: ...
def extract_labels(f, one_hot = ..., num_classes = ...) -> Any: ...
def read_data_sets(train_dir, fake_data = ..., one_hot = ..., dtype = ..., reshape = ..., validation_size = ..., seed = ...) -> Any: ...
