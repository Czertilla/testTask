from .mixins import TimestampMixin, UUIDMixin
from django.db.models import (
    CharField,
    FileField
)
from libabook.storages import PrivateMediaStorage

class Book(UUIDMixin, TimestampMixin):
    title = CharField(max_length=64)
    author = CharField(max_length=64)
    text = FileField(blank=True, storage=PrivateMediaStorage())
