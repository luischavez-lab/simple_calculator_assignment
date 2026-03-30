import pytest
import math
from calculator.calculator import (
    squareNums,
    triNums,
    lazyCaterer,
    magicSquares,
    hypotenuse,
    factorial,
    circleArea,
)


@pytest.mark.parametrize("n, expected", [
    (2, 4),
    (3, 9),
    (5, 25),
])
def test_squareNums(n, expected):
    assert squareNums(n) == expected


@pytest.mark.parametrize("n, expected", [
    (1, 1.0),
    (3, 6.0),
    (5, 15.0),
])
def test_triNums(n, expected):
    assert triNums(n) == expected


@pytest.mark.parametrize("n, expected", [
    (0, 1.0),
    (2, 4.0),
    (4, 11.0),
])
def test_lazyCaterer(n, expected):
    assert lazyCaterer(n) == expected


@pytest.mark.parametrize("n, expected", [
    (1, 1.0),
    (2, 5.0),
    (3, 15.0),
])
def test_magicSquares(n, expected):
    assert magicSquares(n) == expected


@pytest.mark.parametrize("a, b, expected", [
    (3, 4, 5.0),
    (5, 12, 13.0),
    (8, 15, 17.0),
])
def test_hypotenuse(a, b, expected):
    assert hypotenuse(a, b) == pytest.approx(expected)


@pytest.mark.parametrize("n, expected", [
    (0, 1),
    (5, 120),
    (7, 5040),
])
def test_factorial(n, expected):
    assert factorial(n) == expected


@pytest.mark.parametrize("r, expected", [
    (1, math.pi),
    (2, math.pi * 4),
    (3, math.pi * 9),
])
def test_circleArea(r, expected):
    assert circleArea(r) == pytest.approx(expected)
