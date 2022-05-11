from functools import reduce
from math import pi


def fact2(n: int):
    return reduce(int.__mul__, range(n, 0, -2), 1)


def fact(n: int):
    return reduce(int.__mul__, range(n, 0, -1), 1)


def calculate_pi(n: int) -> float:
    """
    n - calculate PI value using n steps
    """
    return 2 * sum([
        fact(k) / fact2(2*k + 1) for k in range(n+1)
    ])


def calculate_approximation_step(e: int) -> int:
    """
    e - calculate count of steps needed to have accuracy in e digits
    """
    approx_pi = 0
    n = 0
    delta = 0
    while abs(approx_pi - pi) > (0.1 ** e):
        n += 1
        approx_pi = calculate_pi(n)
        delta = abs(approx_pi - pi)
    print(f"{approx_pi=}\n{pi=}\n{delta=}\n{n=}")
    return n


digits = int(input("True digits needed: "))
print(calculate_approximation_step(digits))

input()
