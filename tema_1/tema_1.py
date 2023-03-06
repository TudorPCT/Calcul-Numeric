import random

import numpy as np

from strassen_matrix_multiplication import multiply_strassen


def exercise_1():
    m = 1
    x = 1
    while 1 != 1 + 10**-m:
        m += x
    return 10**-(m-x)


def exercise_2_a():
    x = 1.0
    y = exercise_1()
    z = exercise_1()
    return (x + y) + z == x + (y + z)


def exercise_2_b():
    x = random.uniform(0, 1)
    y = random.uniform(0, 1)
    z = random.uniform(0, 1)
    while (x * y) * z == x * (y * z):
        x = random.uniform(0, 1)
        y = random.uniform(0, 1)
        z = random.uniform(0, 1)
    print(f"({x} * {y}) * {z} == {x} * ({y} * {z}) -> {(x * y) * z == x * (y * z)}")


if __name__ == '__main__':
    print(exercise_1())
    print(exercise_2_a())
    exercise_2_b()

    a = [[10, 20, 10], [4, 5, 6], [2, 3, 5]]
    b = [[3, 2, 4], [3, 3, 9], [4, 4, 2]]

    print("Numpy:", np.matmul(a, b))
    c = multiply_strassen(a, b, len(a), 1)
    print("Strassen:", c)

    a = [[5, 7, 9, 10], [2, 3, 3, 8], [8, 10, 2, 3], [3, 3, 4, 8]]
    b = [[3, 10, 12, 18], [12, 1, 4, 9], [9, 10, 12, 2], [3, 12, 4, 10]]

    print("Numpy:", np.matmul(a, b))
    c = multiply_strassen(a, b, len(a), 1)
    print("Strassen:", c)
