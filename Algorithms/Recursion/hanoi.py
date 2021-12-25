#!/usr/bin/env python


def hanoi(n: int, a: str, b: str, c: str) -> None:  # n object Moving from a to c by b
    if n > 0:
        hanoi(n-1, a, c, b)  # (n-1) object Moving from a to b by c
        print(f'Moving from {a} to {c}')  # 1 object Moving from a to c
        hanoi(n-1, b, a, c)  # (n-1) object Moving from b to c by a


hanoi(3, 'A', 'B', 'C')
