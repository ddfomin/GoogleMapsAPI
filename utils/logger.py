import datetime
import os
from requests import Response


class Logger:
    log_dir = "logs"
    _log_file = None  # Будет хранить путь к ЕДИНСТВЕННОМУ файлу

    @classmethod
    def _get_log_file(cls):
        """Создаёт ОДИН файл для всей сессии тестов"""
        if cls._log_file is None:
            # Создаём папку
            os.makedirs(cls.log_dir, exist_ok=True)

            # Создаём ОДИН файл (один раз)
            timestamp = datetime.datetime.now().strftime("%Y-%m-%d_%H-%M-%S")
            cls._log_file = os.path.join(cls.log_dir, f"log_{timestamp}.log")

            # Пишем заголовок в новый файл
            with open(cls._log_file, 'a', encoding='utf-8') as f:
                f.write(f"{'=' * 60}\n")
                f.write(f"Запуск тестов: {datetime.datetime.now()}\n")
                f.write(f"{'=' * 60}\n")

        return cls._log_file

    @classmethod
    def write_log_to_file(cls, data: str):
        """Запись данных в лог-файл"""
        file_name = cls._get_log_file()  # Всегда возвращает один и тот же файл

        with open(file_name, 'a', encoding='utf-8') as logger_file:
            logger_file.write(data)

    @classmethod
    def add_request(cls, url: str, method: str):
        test_name = os.environ.get('PYTEST_CURRENT_TEST', 'Unknown test')

        data_to_add = f"\n{'-' * 60}\n"
        data_to_add += f"Test: {test_name}\n"
        data_to_add += f"Time: {datetime.datetime.now()}\n"
        data_to_add += f"Request: {method} {url}\n"

        cls.write_log_to_file(data_to_add)

    @classmethod
    def add_response(cls, result: Response):
        data_to_add = f"Response code: {result.status_code}\n"
        data_to_add += f"Response body: {result.text}\n"
        data_to_add += f"{'=' * 60}\n"

        cls.write_log_to_file(data_to_add)