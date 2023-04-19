from rest_framework import pagination
from rest_framework.response import Response

class CustomPagination(pagination.LimitOffsetPagination):
    default_limit = 3
    page_size = 3
    limit_query_param = 'l'
    offset_query_param = 'o'
    page_size_query_param = 'page_size'
    max_limit = 50
    min_limit = 1
    max_offset = 50
    min_offset = 3

    def get_paginated_response(self, data):
        response = Response(data)
        response['count'] = self.page.paginator.count
        response['next'] = self.get_next_link()
        response['previous'] = self.get_previous_link()
        return response