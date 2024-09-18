from typing import TYPE_CHECKING
from .mixins import TimestampMixin, UUIDMixin
from django.db.models import (
    CharField,
    FileField, 
    ManyToManyField
)
from libabook.storages import PrivateMediaStorage

if TYPE_CHECKING:
    from .library import Library

class Book(UUIDMixin, TimestampMixin):
    title = CharField(max_length=64)
    author = CharField(max_length=64)
    text = FileField(blank=True, storage=PrivateMediaStorage())
    libraries = ManyToManyField("Library", through="LibraryToBook")