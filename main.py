# main.py

from config import main_menu, search_menu, status_menu
from controllers import Library, validate_int, validate_string, validate_year
from storage import JSONStorage
from utils import show_menu


def main() -> None:
    """
    Главная функция для запуска приложения управления библиотекой.
    """
    storage = JSONStorage()
    library = Library(storage=storage)

    while True:

        choice = show_menu(main_menu)
        if choice == 1:

            title = validate_string(input("Введите название книги: "))
            author = validate_string(input("Введите автора книги: "))
            year = validate_year(input("Введите год издания: "))
            if year:
                library.add_book(title=title, author=author, year=year)

        elif choice == 2:
            try:
                book_id = validate_int(input("Введите ID книги для удаления: "))
                library.delete_book(book_id=book_id)
            except ValueError as e:
                print(f"Ошибка: {e}")

        elif choice == 3:
            print("\nВыберите критерий для поиска:")
            criterion_index = show_menu([item[1] for item in search_menu])
            criterion, display_name = search_menu[criterion_index - 1]
            if criterion == "back":
                print("Возврат в главное меню.")
                continue

            value = input(f"\nВведите запрос в поле {display_name}: ")
            print(criterion, value)
            results = library.search_books(**{criterion: value})

            library.display_books(results)

        elif choice == 4:
            library.display_books()

        elif choice == 5:
            try:
                book_id = validate_int(input("Введите ID книги: "))
                book = library.find_book_by_id(book_id)
                if book:
                    status = show_menu(status_menu)
                    library.change_status(book=book, status=status)
                else:
                    print("Книга с таким ID не найдена.")
            except ValueError as e:
                print(f"Ошибка: {e}")
        elif choice == 6:
            print("Выход из программы.")
            break


if __name__ == "__main__":
    main()
