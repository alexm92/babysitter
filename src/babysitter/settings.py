from __future__ import absolute_import

import os


DB = {
    'name': 'test',
    'host': 'mongodb.local',
    'port': 27017,
}

DEBUG = True

STATIC_PATH = '/Users/alexm/repos/babysitter/web'
TEMPLATE_PATH = '/Users/alexm/repos/babysitter/web'

SERVER_SETTINGS = {
	'static_path': STATIC_PATH,
	'template_path': TEMPLATE_PATH,
	'debug': DEBUG,
	'cookie_secret': '__TODO:_GENERATE_YOUR_OWN_RANDOM_VALUE_HERE__',
}

