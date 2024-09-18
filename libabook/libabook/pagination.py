import math

from dataclasses import dataclass
from dataclasses_json import dataclass_json
from typing import Any
from rest_framework.pagination import PageNumberPagination
from rest_framework.response import Response


@dataclass_json
@dataclass
class PaginationResponse:
    count: int
    next: int
    previous: int
    page_number: int
    num_of_pages: int
    page_size: int
    results: Any

class NumberPagination(PageNumberPagination):
    page_size_query_param = 'page_size'
    max_page_size = 100

    def get_paginated_response(self, data):
        pagination_response = PaginationResponse(
            count=self.page.paginator.count,
            next=self.page.next_page_number() if self.page.has_next() else None,
            previous=self.page.previous_page_number() if self.page.has_previous() else None,
            page_number=self.page.number,
            num_of_pages=math.ceil(self.page.paginator.count / self.get_page_size(self.request)),
            results=data,
            page_size=self.get_page_size(self.request),
        ).to_dict()

        return Response(pagination_response)