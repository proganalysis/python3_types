import pickle
import cloudpickle
import socket
import struct

from flowlight.core.setting import Setting
from flowlight.exceptions import RemoteWorkerNotRunning


def dumps(obj):
    return cloudpickle.dumps(obj)


def loads(data):
    return pickle.loads(data)


class RemoteCallable:
    def __init__(self, callable_obj, *args, **kwargs):
        self.callable = callable_obj
        self.args = args
        self.kwargs = kwargs


class RemoteWorkerMixin:
    def run_remote_callable(self, callable_obj, *args, **kwargs):
        if not callable(callable_obj):
            raise Exception('Need a callable object')
        data = dumps(RemoteCallable(callable_obj, *args, **kwargs))
        client = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        try:
            client.connect((self.host, Setting.PORT))
        except ConnectionRefusedError:
            raise RemoteWorkerNotRunning('Workers on {} not running'.format(self.host))
        client.sendall(struct.pack('>i', len(data)) + data)
        result = b''
        while True:
            stream_data = client.recv(1024)
            if not stream_data:
                break
            result += stream_data
        if not result:
            print('Server has closed the connetion')
            result = ''
        else:
            result = loads(result)
        client.close()
        return result
