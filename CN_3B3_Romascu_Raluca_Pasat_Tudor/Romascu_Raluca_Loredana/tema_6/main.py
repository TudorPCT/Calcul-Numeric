import random
from math import sin, cos

from matplotlib import pyplot as plt


def generate_x(a, b, n):
    x = [random.uniform(a+0.0001, b-0.0001) for _ in range(1, n)]
    x.append(a)
    x.append(b)
    x.sort()
    return x


def f1(x):
    return x**2 - 12 * x + 30


def f2(x):
    return sin(x) - cos(x)


def f3(x):
    return 2 * x**3 - 3 * x + 15


def draw_plot(x_v, y_v, lagrange_y, title):
    line1, = plt.plot(x_v, y_v, label='functia')
    line2, = plt.plot(x_v, lagrange_y, label='')
    plt.legend(handles=[line1, line2])
    plt.title(title)
    plt.show()


def newton_form(x_vector, y_vector, x):
    # diferente divizate
    n = len(x_vector)
    for i in range(1, n):
        for j in range(n - 1, i - 1, -1):
            y_vector[j] = (y_vector[j] - y_vector[j - 1]) / (x_vector[j] - x_vector[j - i])
    # Lagrange form
    lnx = 0
    for i in range(n):
        prod = 1
        for j in range(i):
            prod = prod * (x-x_vector[j])
        lnx = lnx + y_vector[i] * prod
    return lnx


if __name__ == '__main__':
    # ex1
    x_vector = generate_x(1, 5, 10)
    y = [f1(x_vector[i]) for i in range(len(x_vector))]
    y_vector = y
    x = 2
    lagrange = newton_form(x_vector, y_vector, x)
    print(f"Lagrange({x}): ", lagrange)
    print(f"f({x})", f1(x))
    y_lagrange = [newton_form(x_vector, y_vector, x_vector[i]) for i in range(len(x_vector))]
    print(y_lagrange)
    draw_plot(x_vector, y_vector, y_lagrange, "Exemplu 1")

    #ex2
    x_vector = generate_x(0, 1.5, 10)
    y = [f2(x_vector[i]) for i in range(len(x_vector))]
    y_vector = y
    x = 0.7
    lagrange = newton_form(x_vector, y_vector, x)
    print(f"Lagrange({x}): ", lagrange)
    print(f"f({x})", f2(x))
    y_lagrange = [newton_form(x_vector, y_vector, x_vector[i]) for i in range(len(x_vector))]
    draw_plot(x_vector, y_vector, y_lagrange, "Exemplu 2")

    #ex3
    x_vector = generate_x(0, 2, 10)
    y = [f3(x_vector[i]) for i in range(len(x_vector))]
    y_vector = y
    x = 1
    lagrange = newton_form(x_vector, y_vector, x)
    print(f"Lagrange({x}): ", lagrange)
    print(f"f({x})", f3(x))
    y_lagrange = [newton_form(x_vector, y_vector, x_vector[i]) for i in range(len(x_vector))]
    draw_plot(x_vector, y_vector, y_lagrange, "Exemplu 3")

