from __future__ import absolute_import

import logging

from tornado.web import RequestHandler


log = logging.getLogger(__name__)

class ApiController(RequestHandler):
    def get(self, request_url):
        log.info(['alexm: 000000000', request_url])
        self.write({'url': request_url})

