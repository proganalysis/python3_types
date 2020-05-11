import unittest
import chubby.config as config
import os
import configparser

class ConfigTest(unittest.TestCase):

    def test_get_config_path(self):
        self.assertTrue(config.get_config_path().endswith('.chubby'))
        if os.name is 'posix':
            self.assertTrue(config.get_config_path().startswith('/home'))

    def test_create_if_not_exists(self):
        if not os.path.exists(config.get_config_path()):
            config.create_if_not_exists()
        self.assertTrue(os.path.exists(config.get_config_path()))

    def test_read_config(self):
        config_path = os.path.abspath('.chubby.test')
        contents = {
            "key": "value"
        }
        with open('.chubby.test', 'w') as f:
            conf = configparser.ConfigParser()
            conf["test"] = contents
            conf.write(f)
        # read the file
        read = config.read_config(path=config_path)
        self.assertEqual(read["test"]["key"], "value")
        # delete the file
        os.remove(config_path)

    def test_write_config(self):
        config_path = os.path.abspath('.chubby.test.')
        open(config_path, 'w').write("") # create new file

        # testing new section creation
        contents = {
            "key": "value"
        }
        config.write_config("test", contents, path=config_path)

        with open(config_path, 'r') as f:
            self.assertEqual(f.read(), "[test]\nkey = value\n\n")

        # testing updating key of existing section and appending new keys
        contents = {
            "key": "something",
            "key2": "value"
        }
        config.write_config("test", contents, path=config_path)

        with open(config_path, 'r') as f:
            self.assertEqual(f.read(), "[test]\nkey = something\nkey2 = value\n\n")
        os.remove(config_path)
