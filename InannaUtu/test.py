import pytest
from src import inanna_utu

# Test names are anonymised: the test conditions alone will shape results!

def test_a():
    for n in [3, 6, 9, 27, 96, 72, 57, 117]:
        assert inanna_utu(n) == "Inanna!"


def test_b():
    for n in [5, 10, 25, 40, 50, 70, 85, 100]:
        assert inanna_utu(n) == "Utu!"


def test_c():
    for n in [15, 30, 45, 60, 75, 90, 105, 120, 135, 150]:
        assert inanna_utu(n) == "Inanna Utu!"

def test_d():
    for n in [2, 4, 8, 11, 13, 14, 16, 19, 31, 32, 71, 98]:
        assert inanna_utu(n) == f"{n}"

