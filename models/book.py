from dataclasses import dataclass


@dataclass
class Book:
    """
    Определяет книгу в библиотеке.
    """

    id: int
    title: str
    author: str
    year: int
    status: str = "в наличии"

    def to_dict(self) -> dict:
        """
        Преобразует экземпляр книги в словарь.

        :return: Словарь с данными книги.
        """
        return {
            "id": self.id,
            "title": self.title,
            "author": self.author,
            "year": self.year,
            "status": self.status,
        }

    @staticmethod
    def from_dict(data: dict) -> "Book":
        """
        Создает экземпляр книги из словаря.

        :param data: Словарь с данными книги.
        :return: Экземпляр класса Book.
        """
        return Book(
            id=data["id"],
            title=data["title"],
            author=data["author"],
            year=data["year"],
            status=data.get("status", "в наличии"),
        )