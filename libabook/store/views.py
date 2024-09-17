from utils.s3_client import S3Client
from os import getenv
from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework.request import Request
from rest_framework.viewsets import ModelViewSet
from store.serializers import LibrarySerializer, BookSerializer
from django.shortcuts import get_object_or_404

s3 = S3Client(
    getenv('S3_ACCESS_KEY'),
    getenv('S3_SECRET_KEY'),
    endpoint_url=getenv("S3_ENDPOINT_URL"),
    bucket_name=getenv("S3_BUCKET_NAME")
)


class LibraryViewSet(ModelViewSet):
    serializer_class = LibrarySerializer
    queryset = LibrarySerializer.Meta.model.objects.all()


class BookViewSet(ModelViewSet):
    serializer_class = BookSerializer
    queryset = BookSerializer.Meta.model.objects.all()