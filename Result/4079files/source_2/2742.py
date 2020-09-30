#!/usr/bin/env python
# -*- coding: utf-8 -*-

import os
import logging
from tornado import web, options
from handlers import HelloAPIHandler, EchoAPIHandler, MainHandler
from tools import server

abspath = os.path.abspath(__file__)
dname = os.path.dirname(abspath)
os.chdir(dname)

# app's title
__title__ = 'Micro-Service Squeleton'

options.define('port', default=8080, help='run on the given port', type=int)
options.define('logfile', default=None, help='file to write log', type=str)
options.define('verbosity', default='INFO', help='log verbosity : CRITICAL, ERROR, WARNING, INFO, DEBUG', type=str)
options.parse_command_line(final=False)
logging.basicConfig(filename=options.options.logfile, level=options.options.verbosity)
logger = logging.getLogger(__name__)


def main():
    settings = {
        'static_path': './static',
        'template_path': './templates',
    }
    logger.debug('app settings defined')
    application = web.Application([
            (r'/', MainHandler),  # index.html
            (r'/api/hello', HelloAPIHandler),
            (r'/api/echo(.*)$', EchoAPIHandler),
        ], **settings)
    logger.debug('tornado web application created')
    logger.info('tornado web application will be launched on port : ' + str(options.options.port))
    server.start_http(app=application, http_port=options.options.port)


if __name__ == '__main__':
    main()
