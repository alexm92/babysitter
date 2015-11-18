from __future__ import absolute_import

import logging

from tornado.web import RequestHandler


log = logging.getLogger(__name__)

class BaseController(RequestHandler):
    def get_current_user(self):
        return self.get_secure_cookie('user')

