from rest_framework.pagination import PageNumberPagination, CursorPagination


class CursorPagination(CursorPagination):
    page_size = 2
    ordering = 'name'
