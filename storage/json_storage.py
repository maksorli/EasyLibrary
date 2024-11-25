import json
import os

from config import file_path
from models import Book


class JSONStorage:
    """
    Класс для работы с хранением данных в формате JSON.
    """

    def __init__(self, file_path: str = file_path) -> None:
        """
        Инициализирует класс JSONStorage.

        :param file_path: Путь к файлу с данными JSON.
        """
        self.file_path = file_path

        if not os.path.exists(self.file_path):
            # Если файл отсутствует, создаем его с пустым JSON
            with open(self.file_path, "w", encoding="utf-8") as f:
                json.dump({}, f, ensure_ascii=False, indent=4)

    def load(self) -> list[Book]:
        """
        Загружает список книг из JSON файла.

        :return: Список экземпляров класса Book.
        """
        if os.path.exists(self.file_path):
            with open(self.file_path, "r", encoding="utf-8") as f:
                data = json.load(f)
                return [Book.from_dict(book_data) for book_data in data]
        return []

    def save(self, books: list[Book]) -> None:
        """
        Сохраняет список книг в JSON файл.

        :param books: Список экземпляров класса Book.
        """
        try:
            os.makedirs(os.path.dirname(self.file_path), exist_ok=True)
            with open(self.file_path, "w", encoding="utf-8") as f:
                json.dump(
                    [book.to_dict() for book in books],
                    f,
                    ensure_ascii=False,
                    indent=4,
                )

        except Exception as e:
            print(f"Error while saving to file {self.file_path}: {e}")
