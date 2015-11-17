from __future__ import absolute_import

from motorengine.connection import connect
import tornado

from babysitter.settings import DB


# Connect to MongoDB server
io_loop = tornado.ioloop.IOLoop.instance()
connect(DB['name'], host=DB['host'], port=DB['port'], io_loop=io_loop)

from .user import *
from .issue import *
