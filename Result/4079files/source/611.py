import json
import logging
from abc import ABCMeta, abstractmethod

import requests

logger = logging.getLogger('django')


class AbstractDevice(metaclass=ABCMeta):
    """
    Ensure that every device class implements open(), next() and close().
    """

    @abstractmethod
    def open(self):
        pass

    @abstractmethod
    def next(self):
        pass

    @abstractmethod
    def close(self):
        pass


class OverheadDisplay(AbstractDevice):
    def __init__(self, ip_address, *args, **kwargs) -> None:
        self.ip_address = ip_address

    def _request(self, method: str):
        # TODO: document API responses
        payload = {'method': method, 'id': 1, 'params': []}
        headers = {'Content-Type': 'application/json'}
        url = 'http://{}:8888/jsonrpc'.format(self.ip_address)
        try:
            response = requests.post(
                url, data=json.dumps(payload), headers=headers, timeout=0.5
            )
            return response.json().get('result', response.json().get('error'))
        except Exception:
            logger.exception('Error while contacting overhead display.')

    def open(self):
        return self._request('open')

    def next(self):
        return self._request('next')

    def close(self):
        return self._request('close')


class DummyDevice(AbstractDevice):
    def __init__(self, *args, **kwargs) -> None:
        self.logger = logging.getLogger('django')

    def open(self) -> None:
        self.logger.info('[DummyDisplay] Cashdesk has been opened.')

    def next(self) -> None:
        self.logger.info('[DummyDisplay] Cashdesk is ready for the next transaction.')

    def close(self) -> None:
        self.logger.info('[DummyDisplay] Cashdesk has been closed.')
