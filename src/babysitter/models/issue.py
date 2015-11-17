from __future__ import absolute_import

from motorengine import Document, UUIDField, StringField, EmailField, DateTimeField, ReferenceField

from babysitter.models.user import User


class Issue(Document):
    __collection__ = 'issues'

    id = UUIDField()
    title = StringField(required=True)
    content = StringField(required=True)
    level = StringField(required=True)
    date_added = DateTimeField(required=True, auto_now_on_insert=True)
    date_updated = DateTimeField(required=True, auto_now_on_update=True)
    user = ReferenceField(User)

