import json
from datetime import datetime


class SimpleDict(json.JSONEncoder):
    def default(self, o):
        return o.__dict__


class DictOrDateTime(json.JSONEncoder):
    def default(self, o):
        try:
            return o.__getstate__()
        except AttributeError:
            return o.__dict__


class ReservationDecoder(json.JSONDecoder):
    def __init__(self, *args, **kwargs):
        json.JSONDecoder.__init__(self, object_hook=self.object_hook, *args, **kwargs)

    def object_hook(self, obj):
        if '_type' not in obj:
            return obj
        if obj['_type'] == 'datetime':
            return datetime.strptime(obj['value'], '%X')
        return obj