from uuid import UUID
from rest_framework.decorators import action
from rest_framework.response import Response
from rest_framework.request import Request
from rest_framework.viewsets import ModelViewSet
from store.serializers import BookSerializer, LibrarySerializer
from rest_framework.status import HTTP_400_BAD_REQUEST
from django.db.models import Manager
from libabook.pagination import NumberPagination, NumberPaginatorInspector
from rest_framework.parsers import MultiPartParser, FileUploadParser
from drf_yasg.utils import swagger_auto_schema 


class LibraryViewSet(ModelViewSet):
    serializer_class = LibrarySerializer
    queryset = serializer_class.Meta.model.objects.all()

    @action(methods=["GET"], detail=True)
    def books(self, request: Request, pk: UUID) -> Response:
        lib = self.get_object()
        books: Manager = getattr(lib, "books")  
        queryset = books.all()
        page = self.paginate_queryset(queryset)
        serializer = BookSerializer(page, many=True)
        # if serializer.is_valid(): 
        if True: # TODO fix and replace this line by upper one
            return self.get_paginated_response(serializer.data)
        else:
            return Response(
                serializer.errors,
                status=HTTP_400_BAD_REQUEST
            )


class BookViewSet(ModelViewSet):
    parser_classes = [MultiPartParser, FileUploadParser]
    serializer_class = BookSerializer
    queryset = BookSerializer.Meta.model.objects.all()


    @swagger_auto_schema(paginator_inspectors=[NumberPaginatorInspector,])
    @action(methods=["GET"], detail=True, pagination_class = NumberPagination)
    def libraries(self, request: Request, pk: UUID) -> Response:
        obj = self.get_object()
        libraries: Manager = getattr(obj, "libraries")
        queryset = libraries.all()
        page = self.paginate_queryset(queryset)
        serializer = BookSerializer(page, many=True)
        # if serializer.is_valid(): 
        if True: # TODO fix and replace this line by upper one
            return self.get_paginated_response(serializer.data) 
        else:
            return Response(
                serializer.errors,
                status=HTTP_400_BAD_REQUEST
            )