from tkinter import *
from openvino.inference_engine import IENetwork as IENetwork, IEPlugin as IEPlugin
from skimage import io as io, transform as transform
from typing import Any

GREEN: str
RED: str
NOCOLOR: str
YELLOW: str
GOOGLENET_IR: str
ALEXNET_IR: str
SQUEEZENET_IR: str
LABELS_FILE: str
NCAPPZOO_PATH: str
IMAGE_PATH: Any
LABELS_FILE_PATH: Any
root: Any
filename: Any
NETWORKS: Any
networkname: Any
lblImage: Any

def quit() -> None: ...
def buttonCallBack() -> None: ...
def runInfer() -> None: ...

mEntry: Any
b: Any
l: Any
w: Any
btnInfer: Any
qbtn: Any
