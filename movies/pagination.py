from rest_framework.pagination import PageNumberPagination


class MoviesPagination(PageNumberPagination):
    page_size = 10