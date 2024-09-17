from rest_framework.serializers import ModelSerializer
from store.models import Library, Book


class LibrarySerializer(ModelSerializer):
    class Meta:
        model = Library
        fields = ["id", "name", "adress"]


class BookSerializer(ModelSerializer):
    class Meta:
        model = Book
        fields = ["id", "title", "author", "created_at", "edited_at"]
