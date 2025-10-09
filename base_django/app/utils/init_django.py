def init_django():
    import os
    import sys

    import django

    sys.path.append(os.path.dirname(os.path.dirname(__file__)))  # путь до проекта
    os.environ.setdefault("DJANGO_SETTINGS_MODULE", "core.settings")
    django.setup()

    import logging.config

    from django.conf import settings

    logging.config.dictConfig(settings.LOGGING)
