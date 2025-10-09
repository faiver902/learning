import logging
import os

from django.conf import settings


class ModulePathFileHandler(logging.Handler):
    """
    Обработчик логов, который формирует путь лог-файла на основе record.pathname,
    если он не переопределён в extra (например, extra['custom_path']).
    """

    def __init__(self, base_log_dir="logs", level=logging.NOTSET):
        super().__init__(level)
        self.base_log_dir = base_log_dir
        self._path_cache = {}

    def emit(self, record):
        try:
            module_path = record.__dict__.get("custom_path", record.pathname)

            if "site-packages" in module_path:
                return

            if module_path in self._path_cache:
                log_file_path = self._path_cache[module_path]
            else:
                rel_path = os.path.relpath(module_path, settings.BASE_DIR)
                rel_path_no_ext, _ = os.path.splitext(rel_path)
                log_file_path = os.path.join(
                    self.base_log_dir, rel_path_no_ext + ".log"
                )
                self._path_cache[module_path] = log_file_path

            os.makedirs(os.path.dirname(log_file_path), exist_ok=True)
            with open(log_file_path, "a", encoding="utf-8") as log_file:
                log_file.write(self.format(record) + "\n")
        except Exception:
            self.handleError(record)
