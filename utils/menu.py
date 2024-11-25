def show_menu(options):
    """Отображает меню и возвращает выбор пользователя."""
    print("\nВыберите действие:")
    for i, option in enumerate(options, 1):
        print(f"{i}. {option}")
    while True:
        choice = input("Введите номер действия: ")
        try:
            # Преобразуем ввод пользователя в число
            choice = int(choice)
            if 1 <= choice <= len(options):
                print(choice)
                return choice
            else:
                print(f"Неверный ввод. Введите число от 1 до {len(options)}.")
        except ValueError:
            # Если пользователь ввёл не число, выводим сообщение об ошибке
            print("Ошибка: необходимо ввести целое число.")
