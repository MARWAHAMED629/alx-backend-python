from rest_framework.pagination import PageNumberPagination
from rest_framework.response import Response


class MessagePagination(PageNumberPagination):
    # Default number of messages per page
    page_size = 20

    # Allow the client to set a custom page size using the 'page_size' query parameter
    page_size_query_param = 'page_size'

    # Maximum page size allowed
    max_page_size = 100

    def get_paginated_response(self, data):
        """
        Returns a custom paginated response including:
        - Total count of items
        - URL for the next page
        - URL for the previous page
        - The current page results
        """
        return Response({
            'count': self.page.paginator.count,
            'next': self.get_next_link(),
            'previous': self.get_previous_link(),
            'results': data
        })