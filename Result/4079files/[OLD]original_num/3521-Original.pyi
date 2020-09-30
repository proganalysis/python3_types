# (generated with --quick)

import multiprocessing.context
import multiprocessing.queues
from typing import Any, Type

FaceRecognition: Any
Process: Type[multiprocessing.context.Process]
Queue: Type[multiprocessing.queues.Queue]

class FaceRecognitionProcess(multiprocessing.context.Process):
    _FaceRecognitionProcess__face_recognition: Any
    _FaceRecognitionProcess__input_queue: multiprocessing.queues.Queue
    _FaceRecognitionProcess__output_queue: multiprocessing.queues.Queue
    _FaceRecognitionProcess__stop: bool
    def _FaceRecognitionProcess__get_image(self) -> Any: ...
    def __init__(self, face_recognition, input_queue: multiprocessing.queues.Queue, output_queue: multiprocessing.queues.Queue) -> None: ...
    def process_image(self, image) -> None: ...
    def run(self) -> Any: ...
    def stop_process(self) -> None: ...
