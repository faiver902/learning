import logging
import uuid

from django.http import JsonResponse
from pydantic import ValidationError

from services.exception_services.handlers import EXCEPTION_HANDLERS


def get_handler_for_exception(exc: Exception):
    for exc_class in EXCEPTION_HANDLERS:
        if isinstance(exc, exc_class):
            return EXCEPTION_HANDLERS[exc_class]
    return EXCEPTION_HANDLERS[Exception]


def create_support_uuid():
    try:
        return str(uuid.uuid4())
    except Exception:
        return "unknown"


def unified_error_handler(request, exc: Exception):
    handler = get_handler_for_exception(exc)
    status = handler["status"]
    message = handler["message"]
    support_id = create_support_uuid()

    logger = logging.getLogger("exceptions")
    logger.exception(f"[{type(exc).__name__}] {str(exc)} | support_id={support_id}")

    if isinstance(exc, ValidationError):
        error_message = [
            {"field": ".".join(map(str, err["loc"])), "error": err["msg"]}
            for err in exc.errors()
        ]
    else:
        error_message = f"{message}: {str(exc)}"

    return JsonResponse(
        {"error": error_message, "support_id": support_id}, status=status
    )
