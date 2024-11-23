from controllers import validate_int


def show_menu(options):
    """Отображает меню и возвращает выбор пользователя."""
    print("\nВыберите действие:")
    for i, option in enumerate(options, 1):
        print(f"{i}. {option}")
    while True:
        try:
            choice = validate_int(input("Введите номер действия: "))
            if 1 <= choice <= len(options):
                print(choice)
                return choice
            else:
                print(f"Неверный ввод. Введите число от 1 до {len(options)}.")
        except ValueError as e:
            print(f"Ошибка: {e}")
