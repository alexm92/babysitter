from __future__ import absolute_import

from motorengine import Document, UUIDField, StringField, EmailField, DateTimeField


class User(Document):
    __collection__ = 'users'

    id = UUIDField()
    name = StringField()
    email = EmailField(required=True, unique=True)
    password = StringField(required=True)
    date_added = DateTimeField(required=True, auto_now_on_insert=True)

