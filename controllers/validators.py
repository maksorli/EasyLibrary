def validate_int(value: str, error_message: str = "Введите целое число.") -> int | None:
    """
    Проверяет, что значение может быть преобразовано в целое число.

    :param value: Введенное значение.
    :param error_message: Сообщение об ошибке.
    :return: Преобразованное значение или None, если проверка не пройдена.
    """
    try:
        return int(value)
    except ValueError:
        print(error_message)
        return None


def validate_year(year: str, min_year: int = 0, max_year: int = 2024) -> int | bool:
    """
    Проверяет, что год находится в заданном диапазоне.
    Диапазон выбран для книг написанных в нашей эре.

    :param year: Год для проверки в виде строки.
    :param min_year: Минимально допустимый год.
    :param max_year: Максимально допустимый год.
    :return: Год в виде числа, если он корректен, иначе False.
    """

    year_int = validate_int(year, "Год должен быть целым числом.")

    # Если преобразование не удалось, возвращаем False
    if year_int is None:
        return False

    # Проверяем, что год находится в диапазоне
    if min_year <= year_int <= max_year:
        return year_int

    print(f"Год должен быть в диапазоне от {min_year} до {max_year}.")
    return False
