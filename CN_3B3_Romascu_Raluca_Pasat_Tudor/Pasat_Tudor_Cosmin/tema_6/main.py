import random
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
    x = np.zeros(n+1)
    x[0] = a
    x[n] = b

    for i in range(1, n):
        x[i] = random.uniform(x[i-1], x[n])
        while x[i] == x[i-1]:
            x[i] = random.uniform(x[i-1], x[n])

    return x


def generate_y(x, function):
    return np.array([function(x_i) for x_i in x])


def div_dif(x, y):
    n = len(x)
    for i in range(1, n):
        for j in range(n - 1, i - 1, -1):
            y[j] = (y[j] - y[j - 1]) / (x[j] - x[j - i])


def lagrange_interpolation(x, y, t):
    n = len(x)
    p = 0
    for i in range(n):
        p = p + y[i] * prod([(t - x[j]) for j in range(i)])
    return p


def lagrange_norm(lagrange_x, lagrange_y, x, function):
    return abs(lagrange_interpolation(lagrange_x, lagrange_y, x) - function(x))


def min_square_interpolation(x, y):
    n = 3

    b = np.array([[sum([x[k] ** (i + j) for k in range(n)]) for j in range(n)] for i in range(n)])
    f = np.array([[sum(y[k] * x[k] ** i for k in range(n))] for i in range(n)])

    a = np.linalg.solve(b, f)

    return a


def horner(a, x):
    n = len(a)
    d = a[n - 1]

    for i in range(1, n):
        d = d * x + a[n - 1 - i]

    return d


def min_square_norm(a, x, t, function):
    norm_1 = abs(horner(a, t) - function(t))
    norm_2 = sum([abs(horner(a, x_i) - function(x_i)) for x_i in x])
    return norm_1, norm_2


def draw_plot(function, lagrange_x, lagrange_y, pol, title):

    x = np.linspace(0, 1.5, 10000)

    y = generate_y(x, function)

    y_lagrange = np.array(
        [lagrange_interpolation(
            lagrange_x,
            lagrange_y,
            x_i) for x_i in x]
    )

    y_square = np.array(
        [
            horner(pol, x_i) for x_i in x
        ]
    )

    plt.plot(x, y, label='Functia')
    plt.plot(x, y_lagrange, label='Polinomul Lagrange')
    plt.plot(x, y_square, label='Polinomul de interpolare')

    plt.title(title)
    plt.legend()
    plt.show()


if __name__ == "__main__":

    t = 1.1

    print("Exemplu video:")
    x_video = np.array([0, 2, 3, 4])
    y_video = np.array([1, -3, 10, 49])

    print("y_init: ", y_video)
    div_dif(x_video, y_video)
    print("y: ", y_video)

    print("L(1)=", lagrange_interpolation(x_video, y_video, 1))

    print("----------------------------------------------")

    print("Exemplu 1:")

    x_1 = generate_x(5, 1, 5)
    y_1_init = generate_y(x_1, function_1)
    y_1 = y_1_init.copy()

    div_dif(x_1, y_1)
    print("L(t)=", lagrange_interpolation(x_1, y_1, t))
    print("L_norm(t)=", lagrange_norm(x_1, y_1, t, function_1))

    a_1 = min_square_interpolation(x_1, y_1_init)
    p_1 = horner(a_1, t)
    print("P(t)=", p_1)

    norm_1_1, norm_2_1 = min_square_norm(a_1, x_1, t, function_1)
    print("t != x[i]", np.isin(t, x_1))
    print("P_norm_1(t)=", norm_1_1)
    print("P_norm_2(t)=", norm_2_1)

    draw_plot(function_1, x_1, y_1, a_1, "Exemplu 1")

    print("----------------------------------------------")

    print("Exemplu 2:")
    x_2 = generate_x(5, 0, 1.5)
    y_2_init = generate_y(x_2, function_2)
    y_2 = y_2_init.copy()

    div_dif(x_2, y_2)
    print("L(1)=", lagrange_interpolation(x_2, y_2, t))
    print("L_norm(t)=", lagrange_norm(x_2, y_2, t, function_2))

    a_2 = min_square_interpolation(x_2, y_2_init)
    p_2 = horner(a_2, t)
    print("P(t)=", p_2)

    norm_1_2, norm_2_2 = min_square_norm(a_2, x_2, t, function_2)
    print("t != x[i]", np.isin(t, x_2))
    print("P_norm_1(t)=", norm_1_2)
    print("P_norm_2(t)=", norm_2_2)

    draw_plot(function_2, x_2, y_2, a_2, "Exemplu 2")

    print("----------------------------------------------")

    print("Exemplu 3:")
    x_3 = generate_x(5, 0, 2)
    y_3_init = generate_y(x_3, function_3)
    y_3 = y_3_init.copy()

    div_dif(x_3, y_3)
    print("L(t)=", lagrange_interpolation(x_3, y_3, t))
    print("L_norm(t)=", lagrange_norm(x_3, y_3, t, function_3))

    a_3 = min_square_interpolation(x_3, y_3_init)
    p_3 = horner(a_3, t)
    print("P(t)=", p_3)

    norm_1_3, norm_2_3 = min_square_norm(a_3, x_3, t, function_3)
    print("t != x[i]", np.isin(t, x_3))
    print("P_norm_1(t)=", norm_1_3)
    print("P_norm_2(t)=", norm_2_3)

    draw_plot(function_3, x_3, y_3, a_3, "Exemplu 3")

    print("----------------------------------------------")

