# (generated with --quick)

import multiprocessing.context
import multiprocessing.queues
from typing import Any, Type

FaceRecognition: Any
Process: Type[multiprocessing.context.Process]
Queue: Type[multiprocessing.queues.Queue]

class FaceRecognitionProcess(multiprocessing.context.Process):
    _FaceRecognitionProcess__face_recognition: Any
    _FaceRecognitionProcess__input_queue: Any
    _FaceRecognitionProcess__output_queue: Any
    _FaceRecognitionProcess__stop: bool
    def _FaceRecognitionProcess__get_image(self) -> Any: ...
    def __init__(self, face_recognition, input_queue, output_queue) -> None: ...
    def process_image(self, image) -> None: ...
    def run(self) -> Any: ...
    def stop_process(self) -> None: ...
