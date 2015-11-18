from __future__ import absolute_import

import logging
import tornado

from .base import BaseController
from babysitter.models import Issue


log = logging.getLogger(__name__)

class MainController(BaseController):

    def get(self, *args, **kwargs):
        user = None
        if self.current_user:
            user = tornado.escape.xhtml_escape(self.current_user)

        issues = [
            Issue(level='danger', title='OE system is experiencing trouble', content='The problem appears to be resolved now. It was fixed by temporarily increasing the number of servers, and issuing a restart on all servers. We have also changed the instance type for our nat machine in order to make sure there was no limitation there.'),
            Issue(level='warning', title='OE system is experiencing trouble', content='The problem appears to be resolved now. It was fixed by temporarily increasing the number of servers, and issuing a restart on all servers. We have also changed the instance type for our nat machine in order to make sure there was no limitation there.'),
            Issue(level='info', title='PayPal Option Disabled in Payments', content='Due to an ongoing issue with PayPal, we have disabled the option to pay on Facebook with a PayPal account. Some customers may have received error messages while trying to pay with their PayPal accounts. We will update this message if we receive any updates.'),
            Issue(level='success', title='Webhooks Service Degraded', content='The Webhooks service (formerly known as: Real Time Updates) is experiencing a backend issue that is causing a delay in delivering updates. Our engineers are investigating the issue and will post updates as soon as we know more.'),
        ]

        self.render(
            'index.html', 
            title='Baby Sitter - Status of your Platform',
            user=user,
            issues=issues,
        )

