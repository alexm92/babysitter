from __future__ import absolute_import

import logging

from .base import BaseController


log = logging.getLogger(__name__)


class LoginController(BaseController):
	"""
	Login Handler
	"""
	def post(self):
		self.set_secure_cookie('user', self.get_argument('email'))
		self.redirect('/')

