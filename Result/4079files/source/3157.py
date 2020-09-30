#!/usr/bin/env python

def fibonacci(n: int):
    a, b = 0, 1
    if n == 1:
        return a
    elif n == 2:
        return b

    for i in range(2, n):
        a, b = b, a + b

    return b


print(fibonacci(3))

