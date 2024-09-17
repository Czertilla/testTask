from rest_framework.serializers import ModelSerializer, PrimaryKeyRelatedField
from store.models import Library, Book


class LibrarySerializer(ModelSerializer):
    books = PrimaryKeyRelatedField(
        many=True,
        queryset=Book.objects.all()
    )


    class Meta:
        model = Library
        fields = ["id", "name", "adress", "books"]


class BookSerializer(ModelSerializer):
    # libraries = PrimaryKeyRelatedField(
    #     many=True,
    #     queryset=Library.objects.all()
    # )

    class Meta:
        model = Book
        fields = ["id", "title", "author", "created_at", "edited_at", "text"]
