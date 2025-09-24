from typing import Callable


def add(x: int, y: int) -> int:
    return x + y


def subtract(x: int, y: int) -> int:
    return x - y


def multiply(x: int, y: int) -> int:
    return x * y


def divide(x: int, y: int) -> int | float:
    return x / y if y > 0 else 0


def calculator(x: int, y: int, function: Callable[[int, int], int | float]) -> int | float:
    return function(x, y)


# def calculator(x: int, y: int, function: Callable[[int, int], int | float]) -> None:
#     print(function(x, y))


if __name__ == '__main__':
    result = calculator(2, 3, add)
    print(result)
    # calculator(10, 5, divide)