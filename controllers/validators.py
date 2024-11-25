from typing import Any, Callable

from exceptions import ExitException


def repeat_on_invalid(func: Callable) -> Callable:
    """
    Декоратор, который перехватывает исключения ValueError, вызываемые декорируемой
    функцией,    и позволяет пользователю повторить ввод. Если пользователь вводит
    'exit',     выбрасывается исключение ExitException.

    :param func: Декорируемая функция, которая может выбрасывать ValueError.
    :return: Обёрнутая функция, которая обрабатывает ValueError и позволяет
    повторный ввод.
    """

    def wrapper(*args: Any, **kwargs: Any) -> Any:
        """
        Обёртка для декорируемой функции. Перехватывает ValueError и предлагает
        пользователю         повторить ввод. Если пользователь вводит 'exit',
        выбрасывает ExitException.

        :param args: Позиционные аргументы, передаваемые в декорируемую функцию.
        :param kwargs: Именованные аргументы, передаваемые в декорируемую функцию.
        :return: Результат выполнения декорируемой функции, если ввод корректен.
        :raises ExitException: Если пользователь вводит 'exit'.
        """
        while True:
            try:
                # Выполняем функцию
                return func(*args, **kwargs)
            except ValueError as e:
                print(f"Ошибка: {e}")
                # Даём пользователю возможность выйти
                user_input = input("Введите 'exit' для выхода или попробуйте снова: ")
                if user_input.lower() == "exit":
                    print("Выход из текущего меню.")
                    raise ExitException()  # Выход из декоратора, возвращаем None
                # Обновляем аргументы для следующего вызова
                args = (user_input,) + args[1:]

    return wrapper


@repeat_on_invalid
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


@repeat_on_invalid
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
    year_int = validate_int(year)  # Преобразуем строку в целое число
    if min_year <= year_int <= max_year:
        return year_int
    raise ValueError(f"Год должен быть в диапазоне от {min_year} до {max_year}.")


@repeat_on_invalid
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
    value = value.strip()
    if not (min_length <= len(value) <= max_length):
        raise ValueError(
            error_message
            or f"Строка должна быть от {min_length} до {max_length} символов."
        )

    return value
