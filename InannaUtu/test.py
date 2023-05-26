import pytest
from src import inanna_utu


def test_Inanna_if_divisible_by_3():
    for n in [3, 6, 9, 27, 96, 72, 57, 117]:
        assert inanna_utu(n) == "Inanna!"


def test_Utu_if_divisible_by_5():
    for n in [5, 10, 25, 40, 50, 70, 85, 100]:
        assert inanna_utu(n) == "Utu!"


def test_Inanna_Utu_if_divisible_by_15():
    for n in [15, 30, 45, 60, 75, 90, 105, 120, 135, 150]:
        assert inanna_utu(n) == "Inanna Utu!"

