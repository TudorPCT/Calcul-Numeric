import random
from math import sqrt, sin



def function_1(x):
    return 1 / 3 * x ** 3 - 2 * x ** 2 + 2 * x + 3


def function_2(x):
    return x ** 2 + sin(x)


def function_3(x):
    return x ** 4 - 6 * x ** 3 + 13 * x ** 2 - 12 * x + 4


def derivative_1_1(function, x, h):
    return (3 * function(x) - 4 * function(x - h) + function(x - 2 * h)) / (2 * h)


def derivative_1_2(function, x, h):
    return (-function(x + 2 * h) + 8 * function(x + h) - 8 * function(x - h) + function(x - 2 * h)) / (12 * h)


def derivative_2(function, x, h):
    return (-function(x + 2 * h) + 16 * function(x + h) - 30 * function(x)
            + 16 * function(x - h) - function(x - 2 * h)) / (2 * h ** 2)


def secant_method(function, der_1, target: float = 0, h=10**-5, epsilon=10**-9, kmax=1000):
    d_x = 0
    x_0 = random.uniform(target, target)
    x = random.uniform(target, target)

    while x == x_0:
        x = random.uniform(target - 10, target + 10)

    k = 0

    while True:
        d_x_numarator = (x - x_0) * der_1(function, x, h)
        d_x_numitor = (der_1(function, x, h) - der_1(function, x_0, h))
        d_x = d_x_numarator / d_x_numitor if abs(d_x_numitor) > epsilon else 0

        if abs(d_x_numitor) <= epsilon:
            if abs(der_1(function, x, h)) <= epsilon / 100:
                return x, k
            else:
                d_x = 10 ** -5
        x_0 = x
        x = x - d_x
        k += 1

        if abs(d_x) < epsilon or abs(d_x) > 10 ** 8 or k > kmax:
            break

    if abs(d_x) < epsilon:
        return x, k
    else:
        return None, k


def find_func_min_x(function, der_1, der_2, target: float = 0, h=10**-5, epsilon=10**-9, kmax=1000):
    x, k = secant_method(function, der_1, target, h, epsilon, kmax)

    if x is None:
        return None, k

    while der_2(function, x, h) < 0:
        x, k = secant_method(function, der_1, target, h, epsilon, kmax)

        if x is None:
            return None, k

    return x, k


if __name__ == '__main__':
    print("Functia 1")
    print(find_func_min_x(function_1, derivative_1_1, derivative_2, target=2+sqrt(2)))
    print(find_func_min_x(function_1, derivative_1_2, derivative_2, target=2 + sqrt(2)))

    print("============================================")

    print("Functia 2")
    print(find_func_min_x(function_2, derivative_1_1, derivative_2, target=-0.4501836112948))
    print(find_func_min_x(function_2, derivative_1_2, derivative_2, target=-0.4501836112948))

    print("============================================")

    print("Functia 3")
    print(find_func_min_x(function_3, derivative_1_1, derivative_2, target=1))
    print(find_func_min_x(function_3, derivative_1_2, derivative_2, target=1))

    print("--------------------------------------------")

    print(find_func_min_x(function_3, derivative_1_1, derivative_2, target=2))
    print(find_func_min_x(function_3, derivative_1_2, derivative_2, target=2))

    print("--------------------------------------------")

