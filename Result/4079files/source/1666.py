from grakn import client as gc
import unittest
import json
from typing import Any
from requests import PreparedRequest
import httmock
from httmock import urlmatch, HTTMock
from urllib.parse import parse_qs
from urllib.parse import SplitResult
from requests.exceptions import ConnectionError

query: str = 'match $x sub concept; limit 3;'

expected_response = [
    {'id': 'a', 'label': 'concept'},
    {'id': 'b', 'label': 'entity'},
    {'id': 'c', 'label': 'resource'}
]

error_message: str = 'sorry we changed the syntax again'

mock_uri: str = 'myfavouriteserver.com'
keyspace: str = 'somesortofkeyspace'


class MockEngine:
    def __init__(self, status_code: int, response: Any):
        self.headers: dict = None
        self.body: str = None
        self.params: dict = None

        @urlmatch(netloc=mock_uri, path='^/kb/graql/execute$', method='POST')
        def grakn_mock(url: SplitResult, request: PreparedRequest):
            self.headers = request.headers
            self.body = request.body
            self.params = parse_qs(url.query)
            return httmock.response(status_code, json.dumps(response))

        self._httmock: HTTMock = HTTMock(grakn_mock)

    def __enter__(self):
        self._httmock.__enter__()
        return self

    def __exit__(self, *args, **kwargs):
        self._httmock.__exit__(*args, **kwargs)


def engine_responding_ok() -> MockEngine:
    return MockEngine(status_code=200, response=expected_response)


def engine_responding_bad_request() -> MockEngine:
    return MockEngine(status_code=400, response={'exception': error_message})


class TestGraphConstructor(unittest.TestCase):
    def test_open_accepts_no_arguments(self):
        graph = gc.Graph()
        self.assertEqual(graph.keyspace, 'grakn')
        self.assertEqual(graph.uri, 'http://localhost:4567')

    def test_open_accepts_two_arguments(self):
        graph = gc.Graph('http://www.google.com', 'mykeyspace')
        self.assertEqual(graph.uri, 'http://www.google.com')
        self.assertEqual(graph.keyspace, 'mykeyspace')

    def test_open_accepts_keyword_arguments(self):
        graph = gc.Graph(keyspace='mykeyspace', uri='http://www.google.com')
        self.assertEqual(graph.uri, 'http://www.google.com')
        self.assertEqual(graph.keyspace, 'mykeyspace')


class TestExecute(unittest.TestCase):
    def setUp(self):
        self.graph = gc.Graph(uri=f'http://{mock_uri}', keyspace=keyspace)

    def test_executing_a_valid_query_returns_expected_response(self):
        with engine_responding_ok():
            self.assertEqual(self.graph.execute(query), expected_response)

    def test_executing_a_query_sends_expected_accept_header(self):
        with engine_responding_ok() as engine:
            self.graph.execute(query)
            self.assertEqual(engine.headers['Accept'], 'application/graql+json')

    def test_executing_a_query_sends_query_in_body(self):
        with engine_responding_ok() as engine:
            self.graph.execute(query)
            self.assertEqual(engine.body, query)

    def test_executing_a_query_sends_keyspace_in_params(self):
        with engine_responding_ok() as engine:
            self.graph.execute(query)
            self.assertEqual(engine.params['keyspace'], [keyspace])

    def test_executing_a_query_sends_infer_false_in_params(self):
        with engine_responding_ok() as engine:
            self.graph.execute(query)
            self.assertEqual(engine.params['infer'], ['False'])

    def test_executing_a_query_with_inference_sends_infer_true_in_params(self):
        with engine_responding_ok() as engine:
            self.graph.execute(query, infer=True)
            self.assertEqual(engine.params['infer'], ['True'])

    def test_executing_a_query_sends_materialise_in_params(self):
        with engine_responding_ok() as engine:
            self.graph.execute(query)
            self.assertEqual(engine.params['materialise'], ['False'])

    def test_executing_an_invalid_query_throws_grakn_exception(self):
        throws_error = self.assertRaises(gc.GraknError, msg=error_message)
        with engine_responding_bad_request(), throws_error:
            self.graph.execute(query)

    def test_executing_an_insert_query_returns_expected_response(self):
        with engine_responding_ok():
            self.assertEqual(self.graph.execute(query), expected_response)

    def test_executing_a_query_without_a_server_throws_grakn_exception(self):
        with self.assertRaises(ConnectionError):
            self.graph.execute(query)
