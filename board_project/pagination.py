from rest_framework.pagination import PageNumberPagination


class AdPagination(PageNumberPagination):
    """Пагинация для объявлений.

    Возвращает по 4 объявления на страницу.
    """

    page_size = 4
    page_size_query_param = "page_size"
    max_page_size = 8
