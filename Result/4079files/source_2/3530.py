# -*- coding: utf-8 -*-

import logging
from tornado import web

logger = logging.getLogger(__name__)


class MainHandler(web.RequestHandler):
    """Handle '/' endpoint (root server endpoint).
    """

    def get(self):
        """Handle GET requests. Serve the index web page.
        """
        logger.debug('render index.html file')
        self.render('index.html')
        return
