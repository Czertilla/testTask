from os import getenv
from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework.request import Request
from rest_framework.viewsets import ModelViewSet
from store.serializers import BookSerializer, LibrarySerializer

from rest_framework.parsers import MultiPartParser, FileUploadParser
from django.shortcuts import get_object_or_404

class LibraryViewSet(ModelViewSet):
    serializer_class = LibrarySerializer
    queryset = LibrarySerializer.Meta.model.objects.all()


class BookViewSet(ModelViewSet):
    parser_classes = [MultiPartParser, FileUploadParser]
    serializer_class = BookSerializer
    queryset = BookSerializer.Meta.model.objects.all()