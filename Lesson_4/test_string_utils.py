import pytest
from string_utils import StringUtils

utils = StringUtils()


"""capitilize - принимает на вход текст, делает первую букву заглавной
и возвращает этот же текст"""


@pytest.mark.parametrize("input_string, expected_output", [
                        ("skypro", "Skypro"),
                        ("яндекс", "Яндекс"),
                        ("123", "123"),
                        ("", ""),
                        (" ", " "),
                        ("1тест", "1тест"),
                        ("Обнинск", "Обнинск")
                        ])
def test_capitilize(input_string, expected_output):
    assert utils.capitilize(input_string) == expected_output


"""trim - принимает на вход текст и удаляет пробелы в начале, если они есть"""


@pytest.mark.parametrize("input_string, expected_output", [
                        (" skypro", "skypro"),
                        ("  Яндекс", "Яндекс"),
                        (" ", ""),
                        ("123", "123"),
                        ("", ""),
                        ("тест 1", "тест 1"),
                        ("текст ", "текст ")
                        ])
def test_trim(input_string, expected_output):
    assert utils.trim(input_string) == expected_output


"""to_list - принимает на вход текст с разделителем
и возвращает список строк"""


@pytest.mark.parametrize("string, delimeter, result", [
                        ("чай,кофе,молоко", ",", ["чай", "кофе", "молоко"]),
                        ("1,2,3,4,5", ",", ["1", "2", "3", "4", "5"]),
                        ("улица:фонарь", ":", ["улица", "фонарь"]),
                        ("чай&пирожное", "&", ["чай", "пирожное"]),
                        ("", None, []),
                        ("чай,кофе с молоком", None, ["чай", "кофе с молоком"])
                        ])
def test_to_list(string, delimeter, result):
    if delimeter is None:
        res = utils.to_list(string)
    else:
        res = utils.to_list(string, delimeter)
    assert res == result


"""contains - Возвращает `True`, если строка содержит искомый символ
и `False` - если нет"""


@pytest.mark.parametrize("string, symbol, result", [
                        ("чай", "й", True),
                        ("Tea", "e", True),
                        ("Tea and cofee", "e", True),
                        ("12345", "2", True),
                        ("123", "n", False),
                        ("", "й", False),
                        ("Кофе", "5", False)
                        ])
def test_contains(string, symbol, result):
    res = utils.contains(string, symbol)
    assert res == result


"""delete_symbol - удаляет все подстроки из переданной строки"""


@pytest.mark.parametrize("string, symbol, result", [
                        ("чай", "й", "ча"),
                        ("Tea", "e", "Ta"),
                        ("Tea and cofee", "e", "Ta and cof"),
                        ("12345", "2", "1345"),
                        ("123", "n", "123"),
                        ("", "", ""),
                        ("", "й", ""),
                        ("Кофе", "5", "Кофе")
                        ])
def test_delete_symbol(string, symbol, result):
    res = utils.delete_symbol(string, symbol)
    assert res == result


"""starts_with - возвращает `True`, если строка начинается с заданного символа
и `False` - если нет"""


@pytest.mark.parametrize("string, symbol, result", [
                        ("чай", "ч", True),
                        ("Tea", "T", True),
                        ("12345", "1", True),
                        ("123", "5", False),
                        ("", "S", False),
                        (" чай", "ч", False),
                        ("Tea", "t", False)
                        ])
def test_starts_with(string, symbol, result):
    res = utils.starts_with(string, symbol)
    assert res == result


"""end_with - возвращает `True`, если строка заканчивается заданным символом
и `False` - если нет"""


@pytest.mark.parametrize("string, symbol, result", [
                        ("чай", "й", True),
                        ("Tea", "a", True),
                        ("12345", "5", True),
                        ("123", "5", False),
                        ("", "S", False),
                        ("чай ", "q", False)
                        ])
def test_end_with(string, symbol, result):
    res = utils.end_with(string, symbol)
    assert res == result


"""is_empty - возвращает `True`, если строка пустая и `False` - если нет"""


@pytest.mark.parametrize("string, result", [
                        ("", True),
                        (" ", True),
                        ("  ", True),
                        ("123", False),
                        ("cake", False),
                        (" тортик", False)
                        ])
def test_is_empty(string, result):
    res = utils.is_empty(string)
    assert res == result


"""list_to_string - Преобразует список элементов в строку с указанным
разделителем"""


@pytest.mark.parametrize("string, delimeter, result", [
                        (["чай", "кофе", "молоко"], ",", "чай,кофе,молоко"),
                        (["1", "2", "3", "4", "5"], ",", "1,2,3,4,5"),
                        (["улица", "фонарь"], ":", "улица:фонарь"),
                        (["tea", "cake"], "&", "tea&cake"),
                        ([], None, ""),
                        (["чай", "кофе"], None, "чай, кофе")
                        ])
def test_list_to_string(string, delimeter, result):
    if delimeter is None:
        res = utils.list_to_string(string)
    else:
        res = utils.list_to_string(string, delimeter)
    assert res == result
