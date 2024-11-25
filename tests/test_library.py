from controllers import Library


class MockStorage:
    """
    Mock-класс для подмены JSONStorage в тестах.
    """

    def __init__(self):
        self.data = []

    def load(self):
        return self.data

    def save(self, books):
        self.data = books


def test_add_book():
    storage = MockStorage()
    library = Library(storage)

    # Добавляем книгу
    library.add_book("Книга1", "Автор1", 2020)

    assert len(library.books) == 1
    assert library.books[0].title == "Книга1"
    assert library.books[0].author == "Автор1"
    assert library.books[0].year == 2020
    print("test_add_book passed")


def test_delete_book():
    storage = MockStorage()
    library = Library(storage)

    library.add_book("Кинга1", "Автор1", 2020)
    book_id = library.books[0].id

    library.delete_book(book_id)

    assert len(library.books) == 0
    print("test_delete_book passed")


def test_search_books():
    storage = MockStorage()
    library = Library(storage)

    library.add_book("Книга1", "Автор1", 2010)
    library.add_book("Книга2", "Автор2", 2015)

    results = library.search_books(title="Книга1")
    assert len(results) == 1
    assert results[0].title == "Книга1"

    results = library.search_books(author="Автор2")
    assert len(results) == 1
    assert results[0].author == "Автор2"

    results = library.search_books(author="Автор3")
    assert len(results) == 0

    # Поиск по году
    results = library.search_books(year=2010)
    assert len(results) == 1
    assert results[0].year == 2010

    print("test_search_books passed")


def test_change_status():
    storage = MockStorage()
    library = Library(storage)

    # Добавляем книгу
    library.add_book("Book A", "Author One", 2010)
    book = library.books[0]

    # Меняем статус
    library.change_status(book, 2)
    assert book.status == "выдана"

    library.change_status(book, 1)
    assert book.status == "в наличии"

    print("test_change_status passed")


def test_display_books():
    storage = MockStorage()
    library = Library(storage)

    # Добавляем книги
    library.add_book("Book A", "Author One", 2010)
    library.add_book("Book B", "Author Two", 2015)

    # Проверяем вывод
    library.display_books()
    print("test_display_books passed")


def test_find_book_by_id():
    storage = MockStorage()
    library = Library(storage)

    # Добавляем книгу
    library.add_book("Book A", "Author One", 2010)
    book_id = library.books[0].id

    # Ищем книгу по ID
    book = library.find_book_by_id(book_id)
    assert book is not None
    assert book.title == "Book A"

    # Неверный ID
    book = library.find_book_by_id(999)
    assert book is None

    print("test_find_book_by_id passed")


if __name__ == "__main__":
    test_add_book()
    test_delete_book()
    test_search_books()
    test_change_status()
    test_display_books()
    test_find_book_by_id()
