from __future__ import absolute_import

import logging
import os

from motorengine.connection import connect
import tornado.ioloop
import tornado.options
import tornado.web

from .settings import DB, SERVER_SETTINGS
from .controllers import *



log = logging.getLogger(__name__)

class Application(tornado.web.Application):
    """ 
    Main Application 
    """
    def __init__(self):
        handlers = [
            (r'^/$', MainController),
            (r'^/login$', LoginController),
            (r'^/login$', SubscribeController),
            (r'^/api/v1/(.*)$', ApiController),
            (r'^/static/(.*)$', tornado.web.StaticFileHandler, dict(path=SERVER_SETTINGS['static_path'])),
        ]
        tornado.web.Application.__init__(self, handlers, **SERVER_SETTINGS)
        
        # show requests in stdout
        tornado.options.parse_command_line()


def main():
    app = Application()
    app.listen(8888)

    # Connect to MongoDB server
    io_loop = tornado.ioloop.IOLoop.instance()
    connect(DB['name'], host=DB['host'], port=DB['port'], io_loop=io_loop)

    tornado.ioloop.IOLoop.current().start()



if __name__ == '__main__':
    main()

