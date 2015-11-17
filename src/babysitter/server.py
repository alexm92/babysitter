from __future__ import absolute_import

import logging
import os

import tornado.ioloop
import tornado.options
import tornado.web

from .settings import DEBUG
from .controllers import *


log = logging.getLogger(__name__)

class Application(tornado.web.Application):
    """ 
    Main Application 
    """
    def __init__(self):
        settings = {
            'static_path': os.path.join(os.path.dirname(__file__), '../../web'),
            'debug': DEBUG,
        }

        handlers = [
            (r'^/$', MainController),
            (r'^/api/v1/(.*)$', ApiController),
            (r'^/static/(.*)$', tornado.web.StaticFileHandler, dict(path=settings['static_path'])),
        ]
        tornado.web.Application.__init__(self, handlers, **settings)
        
        # show requests in stdout
        tornado.options.parse_command_line()


def main():
    app = Application()
    app.listen(8888)
    tornado.ioloop.IOLoop.current().start()



if __name__ == '__main__':
    main()
