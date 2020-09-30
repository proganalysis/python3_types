# (generated with --quick)

import model
import numpy
import pathlib
from typing import Any, Type

MLPClassifier: Type[model.MLPClassifier]
Path: Type[pathlib.Path]
SequenceClassifier: Type[model.SequenceClassifier]
ThalNetCell: Type[model.ThalNetCell]
argparse: module
args: argparse.Namespace
input_data: Any
itertools: module
np: module
parser: argparse.ArgumentParser
tf: Any

def GRUCell(num_hidden: int, num_layers = ...) -> Any: ...
def main(batch_size: int = ..., log_path: pathlib.Path = ...) -> None: ...
def plot_image(image: numpy.ndarray, label: str) -> None: ...
def plot_learning_curve(title, ys, zs, labels, ylim = ...) -> Any: ...
def timestamp() -> str: ...
