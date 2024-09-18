from django.db.models import (
    CharField, 
    ManyToManyField, 
    ForeignKey,
    IntegerField,
    CASCADE
)

from .book import Book
from .mixins import TimestampMixin, UUIDMixin

class Library(UUIDMixin):
    name = CharField(max_length=64)
    adress = CharField(max_length=128)
    books = ManyToManyField(Book, through="LibraryToBook")

    class Meta:
        ordering = ['adress']

        def __str__(self):
            adress: str = getattr(self, 'adress', None)
            titles: int = len(getattr(self, 'books', [])) 
            
            return f"Library {getattr(self, 'name', None)} ({adress=}, {titles=})"


class LibraryToBook(UUIDMixin, TimestampMixin):
    library = ForeignKey(Library, on_delete=CASCADE)
    book = ForeignKey(Book, on_delete=CASCADE)

    available = IntegerField(blank=True, null=True)
    booked = IntegerField(default=0, blank=True, null=True)
