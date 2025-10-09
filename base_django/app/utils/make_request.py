import requests
from requests import RequestException


def make_request(params: dict, omdb_base_url: str, logger, **kwargs) -> dict:
    """
    Выполняет GET-запрос к OMDb и возвращает JSON.
    - При HTTP-ошибке поднимает Exception с отключённой исходной причиной (from None),
      чтобы не засорять стек.
    - При ошибке декодирования JSON сохраняет исходную причину (from err) — это полезно для отладки.
    """
    try:
        response = requests.get(omdb_base_url, params=params, **kwargs)

        # Бросит HTTPError, если код не 2xx — это короче и точнее, чем вручную проверять status_code
        try:
            response.raise_for_status()
        except requests.HTTPError:
            logger.warning("OMDb ответ %s: %s", response.status_code, response.text)
            # Прячем исходную причину намеренно (неинтересен внутренний стек requests)
            raise Exception(f"OMDb API вернул {response.status_code}") from None

        # Пытаемся распарсить JSON
        try:
            return response.json()
        except ValueError as err:  # JSONDecodeError в некоторых окружениях = ValueError
            logger.exception("Ошибка при разборе JSON: %s", response.text)
            # Сохраняем исходную причину для отладки
            raise Exception(f"Ошибка при разборе JSON: {response.text}") from err

    except RequestException as err:
        # Любые сетевые/транспортные ошибки requests (Timeout, ConnectionError и т.п.)
        logger.exception("Ошибка при выполнении запроса: %s", err)
        # Сохраняем причину
        raise Exception("Ошибка при выполнении запроса к OMDb") from err
