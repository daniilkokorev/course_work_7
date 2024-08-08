from rest_framework.pagination import PageNumberPagination


class HabitPagination(PageNumberPagination):
    """
    Пагинация привычек. Определяет количестао выводимых привычек.
    """
    page_size = 5
    page_query_param = "page_size"
    max_page_size = 100
