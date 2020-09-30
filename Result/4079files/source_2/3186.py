import yaml
import sys
import io
import os

class SettingsParser(object):
    """Settings parser"""

    def __init__(self, path: str):
        """This method loads a yaml file and put it as a python
           dictionary into 'self.settings'."""
        
        with io.open(path, "r") as settings_file:
            self.settings = yaml.load(settings_file)

    def get_port(self) -> int:
        return self.settings['port']

    def get_ip(self) -> str:
        return self.settings['ip']

    def get_data_path(self) -> str:
        return self.settings['data-path']

    def get_meta_store_engine(self) -> str:
        return self.settings['meta-store']['engine']

    def get_meta_store_name(self) -> str:
        return self.settings['meta-store']['name']
        
            
            
