import math

MAX = 1000
EPS = 10 ** (-6)
H = pow(10, -6)
iterations = 500


def f1(x):
    return (1.0 / 3.0) * pow(x, 3) - 2 * pow(x, 2) + 2 * x + 3


def f2(x):
    return x * x + math.sin(x)


def f3(x):
    return (x ** 4) - 6 * pow(x, 3) + 13 * pow(x, 2) - 12 * x + 4


def g1(f, x, h=H):
    return (3 * f(x) - 4 * f(x - h) + f(x - 2 * h)) / (2 * h)


def g2(f, x, h=H):
    return (-f(x + 2 * h) + 8 * f(x + h) - 8 * f(x - h) + f(x - 2 * h)) / (12 * h)


def f_d2(f, x, h=H):
    return (-f(x + 2 * h) + 16 * f(x + h) - 30 * f(x) + 16 * f(x - h) - f(x - 2 * h)) / (12 * pow(h, 2))


def secante(f, x, x0, g):
    k = 0
    deltax = 1
    while EPS <= abs(deltax) <= pow(10, 8) and k <= MAX:
        gxk = g(f, x)
        gx0k = g(f, x0)
        nominator = gxk - gx0k
        if -EPS <= nominator <= EPS:
            if gxk <= EPS / 100:
                if f_d2(f, x) > 0:
                    deltax = 0
            else:
                deltax = pow(10, -5)
        else:
            deltax = (x - x0) * gxk / nominator
        x0 = x
        x = x - deltax
        k = k + 1
    if abs(deltax) < EPS:
        if f_d2(f, x) > 0:
            return x, f'Numar iteratii: {k}'
    return None, f'Numar iteratii: {k}'


def solve(f):
    x = 0.5
    x0 = 0
    solutions = set()
    for i in range(iterations):
        sol_g1, it = secante(f, x, x0, g2)
        sol_g2, it = secante(f, x, x0, g2)
        print(f"g1 solution: {sol_g1}, {it}, for x = {x} and x init = {x0}")
        print(f"g2 solution: {sol_g2}, {it}, for x = {x} and x init = {x0}")
        x = x + 0.5
        x0 = x0 + 0.5
        if sol_g1 is not None:
            solutions.add(round(sol_g1, 6))
            solutions.add(round(sol_g2, 6))
    print("--------------------------------")
    print(solutions)


if __name__ == '__main__':
    solve(f1)
    solve(f2)
    solve(f3)
