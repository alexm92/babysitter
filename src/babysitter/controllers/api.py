from __future__ import absolute_import

import logging

from .base import BaseController


log = logging.getLogger(__name__)

class ApiController(BaseController):
    def get(self, request_url):
        self.write({'url': request_url})

