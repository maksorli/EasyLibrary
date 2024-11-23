def validate_int(
    value: str, error_message: str = "Ошибка валидации, Введите целое число."
) -> int | None:
    """
    Проверяет, что значение может быть преобразовано в целое число.

    :param value: Введенное значение.
    :param error_message: Сообщение об ошибке.
    :return: Преобразованное значение или None, если проверка не пройдена.
    """
    try:
        return int(value)
    except ValueError:

        raise ValueError(error_message)


def validate_year(year: str, min_year: int = 0, max_year: int = 2024) -> int:
    """
    Проверяет, что год находится в заданном диапазоне.
    Диапазон выбран для книг, написанных в нашей эре.

    :param year: Год для проверки в виде строки.
    :param min_year: Минимально допустимый год.
    :param max_year: Максимально допустимый год.
    :return: Год в виде числа, если он корректен.
    :raises ValueError: Если год некорректен или не в диапазоне.
    """
    try:
        # Преобразуем строку в целое число
        year_int = validate_int(year)

        # Проверяем, что год находится в допустимом диапазоне
        if min_year <= year_int <= max_year:
            return year_int
        else:
            raise ValueError()
    except ValueError:
        # Исключение, если преобразование не удалось или год вне диапазона
        print(
            "Год должен быть целым числом и находиться в диапазоне",
            f"от {min_year} до {max_year}.",
        )


def validate_string(
    value: str, min_length: int = 2, max_length: int = 100, error_message: str = None
) -> str:
    """
    Проверяет, что строка имеет длину в заданном диапазоне.

    :param value: Введенная строка.
    :param min_length: Минимально допустимая длина строки.
    :param max_length: Максимально допустимая длина строки.
    :param error_message: Кастомное сообщение об ошибке.
    :return: Корректная строка.
    :raises ValueError: Если строка не соответствует требованиям.
    """
    while True:
        try:

            value = value.strip()  # Убираем лишние пробелы по краям

            if not (min_length <= len(value) <= max_length):
                raise ValueError(
                    error_message
                    or f"Строка должна быть от {min_length} до {max_length} символов."
                )

            return value  # Возврат корректного значения завершает цикл
        except ValueError as e:
            print(f"Ошибка: {e}")
            value = input("Попробуйте снова: ")  # Запрашиваем новый ввод
