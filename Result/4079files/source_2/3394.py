import unittest
import unittest.mock
import json
from contextlib import closing

from psycopg2 import DatabaseError
from werkzeug.test import Client
from werkzeug.wrappers import BaseResponse

from microservice import users, components, main
from tests.helpers import TestDatabase, generate_name


class TestUsers(unittest.TestCase):

    def setUp(self):
        self._old_redis_key = users.REDIS_KEY
        users.REDIS_KEY = 'microservice-' + generate_name()

    def tearDown(self):
        users.REDIS_KEY = self._old_redis_key

    def test_get_all(self):
        with closing(TestDatabase()) as test_db:
            redis = components.get_redis()
            test_db.use_table('users')
            expected_users = ["user_A", "user_B", "user_C"]
            with unittest.mock.patch('microservice.components.get_psql') as db_mock:
                db_mock.return_value = test_db.connection
                self.assertListEqual(expected_users, users.get_all())
                self.assertEqual(json.dumps(expected_users), redis.get(users.REDIS_KEY))

    def test_get_all_no_connection(self):
        with closing(TestDatabase()) as test_db:
            test_db.use_table('users')
            expected_users = ["user_A", "user_B", "user_C"]
            with unittest.mock.patch('microservice.components.get_psql') as db_mock:
                db_mock.return_value = test_db.connection
                self.assertListEqual(expected_users, users.get_all())
            with unittest.mock.patch('microservice.components.get_psql') as db_mock:
                db_mock.return_value.cursor.side_effect = DatabaseError
                self.assertListEqual(expected_users, users.get_all())


class TestUsersIntegration(unittest.TestCase):

    def setUp(self):
        self._old_redis_key = users.REDIS_KEY
        users.REDIS_KEY = 'microservice-' + generate_name()

    @unittest.mock.patch('microservice.components.get_raven')
    @unittest.mock.patch('microservice.components.get_riemann')
    def test_get_all(self, raven_mock, riemann_mock):
        with closing(TestDatabase()) as test_db:
            test_db.use_table('users')
            with unittest.mock.patch('microservice.components.get_psql') as db_mock:
                db_mock.return_value = test_db.connection

                json_rpc = {
                    "jsonrpc": "2.0",
                    "id": 1,
                    "method": "get_users",
                    "params": []
                }
                client = Client(main.application, BaseResponse)
                response = client.post(data=json.dumps(json_rpc))

                json_rpc_result = {
                    "jsonrpc": "2.0",
                    "result": ["user_A", "user_B", "user_C"],
                    "id": 1
                }

                json_rpc_response = response.get_data(as_text=True)
                self.assertDictEqual(json_rpc_result, json.loads(json_rpc_response))

    def tearDown(self):
        users.REDIS_KEY = self._old_redis_key


if __name__ == '__main__':
    unittest.main()
