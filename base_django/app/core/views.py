from logging import getLogger

from django.db import connection
from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework.views import APIView

logger = getLogger(__name__)


class TestView(APIView):
    def get(self, request):
        return Response({"mess": "Work"})


@api_view(["GET"])
def test_endpoint(request):
    return Response({"message": "Hello from test endpoint!"})


class CountDatabaseQueriesMiddleware:
    def __init__(self, get_response):
        self.get_response = get_response

    def __call__(self, request):
        # Обработка запроса
        response = self.get_response(request)

        # Количество запросов к базе данных
        total_queries = len(connection.queries)

        # Логирование количества запросов
        logger.info(f"Обработано {total_queries} запросов к базе данных.")

        # if total_queries > 0:
        #     logger.info("Список запросов к базе данных:")
        #     for i, query in enumerate(connection.queries):
        #         sql = query['sql']
        #         time = query['time']
        #         logger.info(f"Запрос #{i + 1}:")
        #         logger.info(f"    SQL: {sql}")
        #         logger.info(f"    Время выполнения: {time} секунд")

        return response
