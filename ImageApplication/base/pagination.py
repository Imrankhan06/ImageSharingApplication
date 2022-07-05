from rest_framework.pagination import PageNumberPagination


class FollowersLikersPagination(PageNumberPagination):
    """Pagination for followers like"""
    page_size = 50
    page_size_query_param = 'page_size'
    max_page_size = 5000


class PostsPagination(PageNumberPagination):
    """Pagination for posts"""
    page_size = 10
    page_size_query_param = 'page_size'
    max_page_size = 100
