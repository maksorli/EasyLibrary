from controllers import validate_int, validate_string, validate_year


def test_validate_int():
    assert validate_int("10") == 10
    assert validate_int("-5") == -5

    try:
        validate_int("abc")
    except ValueError as e:
        assert str(e) == "Ошибка валидации, Введите целое число."

    print("test_validate_int passed")


def test_validate_year():
    assert validate_year("2020") == 2020
    assert validate_year("1500", min_year=0, max_year=2024) == 1500

    try:
        validate_year("abcd")
    except ValueError:
        pass

    try:
        validate_year("3000", min_year=0, max_year=2024)
    except ValueError:
        pass

    print("test_validate_year passed")


def test_validate_string():
    assert validate_string("Первый", min_length=2, max_length=100) == "Первый"
    assert validate_string("  Второй  ", min_length=2, max_length=100) == "Второй"

    try:
        validate_string("T", min_length=2, max_length=100)
    except ValueError as e:
        assert "Строка должна быть от" in str(e)

    print("test_validate_string passed")


if __name__ == "__main__":
    test_validate_int()
    test_validate_year()
    test_validate_string()
