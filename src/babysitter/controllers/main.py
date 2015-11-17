from __future__ import absolute_import

import logging

from tornado.web import RequestHandler


log = logging.getLogger(__name__)

class MainController(RequestHandler):
    def get(self, *args, **kwargs):
        self.render('../../../web/index.html', title='Babysitter - Issue tracking')

