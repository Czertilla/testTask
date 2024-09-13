from .mixins import TimestampMixin, UUIDMixin
from django.db.models import (
    CharField
)


class Book(UUIDMixin, TimestampMixin):
    title = CharField(max_length=64)
    author = CharField(max_length=64)
