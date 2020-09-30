import validators
import unittest
import yaml
import sys
import os

# MAKING SURE THAT SETTINGS.YAML IS GOING TO BE FOUND!
TEEKA_SETTINGS = os.getenv('TEEKA_SETTINGS', "../settings.yaml")

# ADDING PARENT AND CURRENT DIRECTORIES INTO SYSTEM PATH
CURREN_DIR = os.path.dirname(os.path.abspath(__file__))
sys.path.append(os.path.join(CURREN_DIR, os.pardir))
sys.path.append(CURREN_DIR)

from server.setting_parser import SettingsParser

class TestStringMethods(unittest.TestCase):

    def setUp(self):
        self.settings_file = TEEKA_SETTINGS
        self.settings_parser_instance = SettingsParser(self.settings_file)

    def tearDown(self):
        pass

    def test_port(self):
        self.assertIsInstance(self.settings_parser_instance.get_port(), int)
        self.assertLess(self.settings_parser_instance.get_port(), 65536)
        self.assertGreater(self.settings_parser_instance.get_port(), 0)

    def test_ip(self):
        self.assertTrue(validators.ipv4(self.settings_parser_instance.get_ip()))

    def test_data_path(self):
        self.assertTrue(os.path.exists(self.settings_parser_instance.get_data_path()))
        self.assertTrue(os.path.isdir(self.settings_parser_instance.get_data_path()))
        self.assertTrue(os.access(self.settings_parser_instance.get_data_path(), os.W_OK))
        self.assertTrue(os.access(self.settings_parser_instance.get_data_path(), os.R_OK))

    def test_meta_store_engine(self):
        meta_stores = ["sqlite3"]
        self.assertIsInstance(self.settings_parser_instance.get_meta_store_engine(), str)
        self.assertIn(self.settings_parser_instance.get_meta_store_engine(), meta_stores)

    def test_meta_store_name(self):
        self.assertIsInstance(self.settings_parser_instance.get_meta_store_name(), str)
        self.assertGreater(len(self.settings_parser_instance.get_meta_store_name()), 0)
        
if __name__ == '__main__':
    unittest.main()
