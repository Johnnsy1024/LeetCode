from typing import Callable


def demo_func(x):
    return -(3 * x**2) - 5 * x - 7


def triple_search(l: int, r: int, epsilon: float, func: Callable):
    while r - l > epsilon:
        m1 = l + (r - l) / 3
        m2 = r - (r - l) / 3
        if func(m1) > func(m2):
            r = m2
        else:
            l = m1
    return (l + r) / 2


if __name__ == "__main__":
    print(triple_search(-10, 10, 0.001, demo_func))
