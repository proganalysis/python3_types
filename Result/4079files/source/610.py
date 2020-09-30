import falcon
import logging
import uuid
import os
import sys

# ADDING PARENT AND CURRENT DIRECTORIES INTO SYSTEM PATH
CURREN_DIR = os.path.dirname(os.path.abspath(__file__))
sys.path.append(os.path.join(CURREN_DIR, os.pardir))
sys.path.append(CURREN_DIR)

from setting_parser import SettingsParser

# MAKING SURE THAT SETTINGS.YAML IS GOING TO BE FOUND!
SETTINGS = os.getenv('TEEKA_SETTINGS', "../settings.yaml")

class Pull(object):
    """ Box-pull logic """

    def __init__(self):
        self.logger = logging.getLogger('Vault.Pull.' + __name__)

        # loading the settings
        self.settings_parser = SettingsParser(SETTINGS)

    def on_get(self, req: falcon.Request, resp: falcon.Response, boxid: str) -> None:
        """ Handling a box-pull request """

        try:
            box_container = self.settings_parser.get_data_path()
            box_path = box_container + "/" + boxid + ".box"

            # stream the box to the client
            resp.content_type = "application/octet-stream"
            resp.stream = open(box_path, "rb")
            resp.stream_len = os.path.getsize(box_path)
                    
        except Exception as error:
            self.logger.error(error)
            resp.status = falcon.HTTP_500
            resp.body = None
        else:
            resp.status = falcon.HTTP_200

if __name__ == '__main__':
    # need this only for testing
    from wsgiref import simple_server
    application = falcon.API()
    application.add_route('/vault/1/pull/{boxid}', Pull())
    server = simple_server.make_server('127.0.0.1', 18000, application)
    server.serve_forever()
