import builtins

import pytest

from unittest import mock

from calculator import add, subtract, multiply, divide,menu

@pytest.mark.parametrize("a, b, expected", [
    (1, 2, 3),
    (0, 0, 0),
    (-1, 1, 0),
    (2, -3, -1),
])
def test_add(a, b, expected):
    assert add(a, b) == expected

@pytest.mark.parametrize("a, b, expected", [
    (1, 2, -1),
    (2, -3, 5),
])
def test_subtract(a, b, expected):
    assert subtract(a, b) == expected

@pytest.mark.parametrize("a, b, expected", [
    (1, 2, 2),
    (0, 0, 0),
    (-1, 1, -1),
    (2, -3, -6),
])
def test_multiply(a, b, expected):
    assert multiply(a, b) == expected

@pytest.mark.parametrize("a, b, expected", [
    (1, 2, 0.5),
    (0, 1, 0),
    (-1, 1, -1),
])
def test_divide(a, b, expected):
    assert divide(a, b) == expected

@pytest.mark.parametrize("choice,a, b", [
    (1,1, 2),
    (2,1, 2),
    (3,1, 2),
    (4,1, 2),
    ("a",1,2)
])
def test_menu(mocker,choice,a,b):
    mock_get_numbers = mocker.patch("calculator._get_numbers",return_value=(a,b))
    mock_add = mocker.patch("calculator.add")
    mock_subtract = mocker.patch("calculator.subtract")
    mock_multiply = mocker.patch("calculator.multiply")
    mock_divide = mocker.patch("calculator.divide")

    builtins.input = lambda _: str(choice)

    menu()

    if choice == 1:
        mock_add.assert_called_once()
    elif choice == 2:
        mock_subtract.assert_called_once()
    elif choice == 3:
        mock_multiply.assert_called_once()
    elif choice == 4:
        mock_divide.assert_called_once()
