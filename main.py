# main.py

from controllers import Library
from storage import JSONStorage


def main() -> None:
    """
    Главная функция для запуска приложения управления библиотекой.
    """
    storage = JSONStorage()
    library = Library(storage=storage)

    while True:
        print("\nВыберите действие:")
        print("1. Добавить книгу")
        print("2. Удалить книгу")
        print("3. Поиск книги")
        print("4. Отобразить все книги")
        print("5. Изменить статус книги")
        print("6. Выход")
        choice = input("Введите номер действия: ")

        if choice == "1":
            title = input("Введите название книги: ")
            author = input("Введите автора книги: ")
            try:
                year = int(input("Введите год издания: "))
                if 0 < year < 2024:
                    library.add_book(title=title, author=author, year=year)
            except ValueError:
                print("Год издания должен быть целым числом.")

        elif choice == "2":
            try:
                book_id = int(input("Введите ID книги для удаления: "))
                if book_id is None:
                    print("Нет книги с таким ID.")
                else:
                    library.delete_book(book_id=book_id)
            except ValueError:
                print("ID должен быть числом.")

        elif choice == "3":
            criteria_map = {
                "1": "title",
                "2": "author",
                "3": "year",
            }

            print("По какому критерию искать книгу?")
            print("1. Название")
            print("2. Автор")
            print("3. Год издания")
            search_choice = input("Введите номер критерия: ")

            if search_choice in criteria_map:
                criterion = criteria_map[search_choice]
                value = input(f"Введите {criterion}: ")

                if criterion == "year":
                    try:
                        value = int(value)
                    except ValueError:
                        print("Год издания должен быть числом.")
                        return
                print(f"{criterion}: {value}")
                results = library.search_books(**{criterion: value})
                print(results)
                library.display_books(results)
            else:
                print("Неверный выбор.")

        elif choice == "4":
            library.display_books()

        elif choice == "5":
            try:
                book_id = int(input("Введите ID книги: "))
                status = input(
                    "Введите новый статус:\n"
                    "1. в наличии\n"
                    "2. выдана\n"
                    "Введите номер действия: "
                )
                library.change_status(book_id=book_id, status=status)
            except ValueError:
                print("ID должен быть числом.")

        elif choice == "6":
            print("Выход из программы.")
            break

        else:
            print("Неверный выбор. Попробуйте снова.")


if __name__ == "__main__":
    main()
