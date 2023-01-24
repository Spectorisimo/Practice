from collections import OrderedDict

from rest_framework.pagination import PageNumberPagination, CursorPagination
from rest_framework.response import Response


class CustomCursorPagination(CursorPagination):
    ordering = '-created_at'
    page_size = 4



class CustomPageNumberPagination(PageNumberPagination):
    page_size = 4
    page_size_query_param = 'page_size'

    def get_paginated_response(self, data):  # убрал значение count
        return Response(OrderedDict([
            ('next', self.get_next_link()),
            ('previous', self.get_previous_link()),
            ('results', data)
        ]))
