from models import Book
from storage import JSONStorage


class Library:
    """
    Класс для управления библиотекой.
    """

    def __init__(self, storage: JSONStorage) -> None:
        """
        Инициализирует класс Library.

        :param storage: Экземпляр класса JSONStorage.
        """
        self.storage = storage
        self.books: list[Book] = self.storage.load()
        self.next_id = self._get_next_id()

    def _get_next_id(self) -> int:
        """
        Определяет следующий доступный ID для новой книги.

        :return: Целое число следующего ID.
        """
        if self.books:
            return max(book.id for book in self.books) + 1
        return 1

    def add_book(self, title: str, author: str, year: int) -> None:
        """
        Добавляет новую книгу в библиотеку.

        :param title: Название книги.
        :param author: Автор книги.
        :param year: Год издания.
        """
        for book in self.books:
            if book.title == title and book.author == author and book.year == year:
                print("Книга с таким названием, автором и годом уже существует.")
                return

        book = Book(id=self.next_id, title=title, author=author, year=year)
        self.books.append(book)
        self.next_id += 1
        self.storage.save(self.books)
        print(f"Книга добавлена с ID {book.id}")

    def delete_book(self, book_id: int) -> None:
        """
        Удаляет книгу из библиотеки по ID.

        :param book_id: ID книги для удаления.
        """
        pass

    def search_books(self, **kwargs) -> list[Book]:
        """
        Ищет книги по заданным критериям.

        :param kwargs: Критерии поиска (title, author, year).
        :return: Список найденных книг.
        """
        pass

    def change_status(self, book_id: int, status: str) -> None:
        """
        Изменяет статус книги.

        :param book_id: ID книги.
        :param status: Новый статус ('в наличии' или 'выдана').
        """
        for book in self.books:
            if book.id == book_id:
                if status == "1":
                    book.status = "в наличии"
                    self.storage.save(self.books)
                    print(f"Статус книги с ID {book_id} изменен на '{status}'.")
                elif status == "2":
                    book.status = "выдана"
                    self.storage.save(self.books)
                    print(f"Статус книги с ID {book_id} изменен на '{status}'.")
                else:
                    print("Некорректный статус. Используйте '1' или '2'.")
                return
        print(f"Книга с ID {book_id} не найдена.")

    def get_all_books(self) -> list[Book]:
        """
        Возвращает список всех книг в библиотеке.

        :return: Список экземпляров класса Book.
        """
        return self.books

    def display_books(self, books: list[Book] = None) -> None:
        pass
