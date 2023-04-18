from math import sin, cos

import numpy as np
from numpy import prod
import matplotlib.pyplot as plt


def function_1(x):
    return x**2 - 12 * x + 30


def function_2(x):
    return sin(x) - cos(x)


def function_3(x):
    return 2 * x**3 - 3 * x + 15


def generate_x(n, a, b):
    return np.linspace(a, b, n+1)


def generate_y(x, function):
    return np.array([function(x_i) for x_i in x])


def div_dif(x, y):
    n = len(x)
    for i in range(1, n):
        for j in range(n - 1, i - 1, -1):
            y[j] = (y[j] - y[j - 1]) / (x[j] - x[j - i])


def draw_plot(a, b, function, lagrange_x, lagrange_y, pol, title):

    x = generate_x(10000, -10, 10)

    y = generate_y(x, function)

    y_lagrange = np.array(
        [newton_interpolation(
            lagrange_x,
            lagrange_y,
            x_i) for x_i in x]
    )

    plt.plot(x, y, label='Functia')
    plt.plot(x, y_lagrange, label='Polinomul Lagrange')

    plt.title(title)
    plt.legend()
    plt.show()


def newton_interpolation(x, y, t):
    n = len(x)
    p = 0
    for i in range(n):
        p = p + y[i] * prod([(t - x[j]) for j in range(i)])
    return p


if __name__ == "__main__":

    print("Exemplu video:")
    x_video = np.array([0, 2, 3, 4])
    y_video = np.array([1, -3, 10, 49])

    print("y_init: ", y_video)
    div_dif(x_video, y_video)
    print("y: ", y_video)

    print("L(1)=", newton_interpolation(x_video, y_video, 1))

    print("----------------------------------------------")

    print("Exemplu 1:")

    x_1 = generate_x(5, 1, 5)
    y_1 = generate_y(x_1, function_1)

    div_dif(x_1, y_1)
    print("L(1)=", newton_interpolation(x_1, y_1, 1))

    draw_plot(1, 5, function_1, x_1, y_1, None, "Exemplu 1")

    print("----------------------------------------------")

    print("Exemplu 2:")
    x_2 = generate_x(5, 0, 1.5)
    y_2 = generate_y(x_2, function_2)

    div_dif(x_2, y_2)
    print("L(1)=", newton_interpolation(x_2, y_2, 1))
    draw_plot(0, 1.5, function_2, x_2, y_2, None, "Exemplu 2")

    print("----------------------------------------------")

    print("Exemplu 3:")
    x_3 = generate_x(5, 0, 2)
    y_3 = generate_y(x_3, function_3)

    div_dif(x_3, y_3)
    print("L(1)=", newton_interpolation(x_3, y_3, 1))
    draw_plot(0, 2, function_3, x_3, y_3, None, "Exemplu 3")

    print("----------------------------------------------")


