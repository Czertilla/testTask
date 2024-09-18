from rest_framework.serializers import ModelSerializer, PrimaryKeyRelatedField, SerializerMethodField
from store.models import Library, Book, LibraryToBook



class LibrarySerializer(ModelSerializer):
    books = PrimaryKeyRelatedField(
        many=True,
        queryset=Book.objects.all(),
        required = False
    )

    class Meta:
        model = Library
        fields = ["id", "name", "adress", "books"]


class BookSerializer(ModelSerializer):
    libraries = PrimaryKeyRelatedField(
        many=True,
        queryset=Library.objects.all(),   
        required = False
    )

    class Meta:
        model = Book
        fields = ["id", "title", "author", "created_at", "edited_at", "text", "libraries"]
