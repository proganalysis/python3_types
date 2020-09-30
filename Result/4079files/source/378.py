#!/usr/bin/python
# -*- coding: utf-8 -*-

""" TODO TBD
"""

# Python-native imports
import logging.config
from http.server import BaseHTTPRequestHandler
import threading
import json

# Third-party imports
import pykka

# App imports
from pyCrow.crowlib import Action
from pyCrow.crowlib.http import Server

L = logging.getLogger(__name__)
L.debug(f'Loaded module: {__name__}.')


class ExperimentActor(pykka.ThreadingActor):
    def __init__(self, config: dict, **kwargs):
        super().__init__()
        self._config = config
        self._view = self._server_thread = None

    def on_start(self):
        L.info(msg=f'Started ExperimentActor ({self.actor_urn})')
        view = self._config.get('view', 'web')
        if view == 'web':
            _address = self._config.get('view_web', {}).get('address', '')
            _port = self._config.get('view_web', {}).get('port', 34567)
            self._view = Server((_address, _port), handler=WebView)
            self._server_thread = threading.Thread(target=self._view.start, daemon=False)
            self._server_thread.start()

    def on_stop(self):
        L.info('ExperimentActor is stopped.')

    def on_failure(self, exception_type, exception_value, traceback):
        L.error(f'ExperimentActor failed: {exception_type} {exception_value} {traceback}')

    def on_receive(self, msg: dict) -> None:
        L.info(msg=f'ExperimentActor received message: {msg}')
        # process msg and alter state accordingly
        _cmd = msg.get('cmd', '').lower()
        if _cmd == Action.MODEL_TRAIN.get('cmd'):
            labels = msg.get('labels', [])
            # TODO check that there are labels, if none
        else:
            # default: do nothing but log this event
            L.info(msg=f'Received message {msg} which cannot be processed.')


class WebView(BaseHTTPRequestHandler):
    def __init__(self, request, client_address, server):
        super().__init__(request, client_address, server)

    def _set_response(self, status_code=200):
        self.send_response(status_code)
        self.send_header('Content-type', 'text/html')
        self.end_headers()

    def do_GET(self):
        _headers = str(self.headers).replace('\n\n', '').replace('\n', ', ')
        L.debug(f'Method: [GET], Path: [{self.path}], Headers: [{_headers}]')
        # TODO refactor into html resource file // template file
        response = '''
        <html>
            <head>
                <title>Experiment View</title>
                <style>
                    .addbutton {cbo}
                        background-color: #d44949;
                        height: 20px;
                        outline: 0;
                        display: block;
                        margin: 10px 0px 0px 5px;
                        color: #fff;
                        border-radius: 100%;
                        width: 20px;
                        text-align: center;
                        font-weight: bold;
                        font-size: 17px;
                    {cbc}
                </style>
                <script>
                function addlabel() {cbo}
                    var newspan = document.createElement('span');
                    newspan.innerHTML = '<br>Label: <input type="text" class="label" />';
                    document.getElementById('foobar').appendChild(newspan);
                {cbc}
                </script>
            </head>
            <body>
                <p>GET Path: {path}</p>
                <div id="foobar">
                    <span>Label: <input type="text" class="label" /></span>
                </div>
                <div class="addbutton" onclick="addlabel()">+</div>
                <p><input type="submit" value="Submit" name="submit" /></p>
            </body>
        </html>
        '''.format(path=self.path, cbo='{', cbc='}')
        self._set_response()
        self.wfile.write(response.encode('utf-8'))

    def do_POST(self):
        # size of data
        content_length = int(self.headers['Content-Length'])
        # POST data itself
        post_data = self.rfile.read(content_length)
        _headers = str(self.headers).replace('\n\n', '').replace('\n', ', ')
        L.debug(f'Method: [POST], Path: [{self.path}], Headers: [{_headers}], '
                f'Body: [{post_data.decode("utf-8")}]')

        # todo validate msg
        msg: dict = json.loads(post_data.decode('utf-8'))
        # fixme check if there is such an actor, send an appropriate REST response?
        try:
            pykka.ActorRegistry.get_by_class_name(msg.get('target', 'AppActor'))[0].tell(msg)
            self._set_response()
            self.wfile.write(str({'error': ''}).encode('utf-8'))
        except IndexError:
            response = f'There is no such target actor {msg.get("target", "appActor")} registered.'
            L.warning(response)
            pykka.ActorRegistry.get_by_class_name('AppActor')[0].tell(msg)
            self._set_response(404)
            self.wfile.write(json.dumps({'error': response}).encode('utf-8'))


class NativeView(object):
    def __init__(self):
        super(NativeView, self).__init__()
        raise NotImplementedError()  # TODO
