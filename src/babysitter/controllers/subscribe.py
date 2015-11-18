from __future__ import absolute_import

import logging

from .base import BaseController


log = logging.getLogger(__name__)


class SubscribeController(BaseController):
	"""
	Subscribe Handler
	"""
	def post(self):
		email = self.get_argument('email')
		log.info(['alexm: *********** subscribe', email])
		self.redirect('/')

