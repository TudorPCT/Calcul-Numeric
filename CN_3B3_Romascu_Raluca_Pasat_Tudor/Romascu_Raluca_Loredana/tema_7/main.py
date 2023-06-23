import math
import random

EPS = pow(10, -7)
MAX = 1000
iterations = 5000


def get_interval(p):
    return (abs(p[0]) + max([abs(pi) for pi in p])) / abs(p[0])


def sign(x):
    if x >= 0:
        return 1
    else:
        return -1


def horner_method(p, x):
    n = len(p)
    bi = p[0]
    for i in range(1, n):
        bi = p[i] + bi * x
        # b = bi
    return bi


def derivate_p(p):
    n = len(p)
    coeffs = [0 for i in range(n - 1)]
    for i in range(n - 1):
        coeffs[i] = (n - 1 - i) * p[i]
    return coeffs


def solve_laguerre(p, x, r):
    k = 0
    delta_xk = 1
    n = len(p)
    while EPS <= abs(delta_xk) <= pow(10, 8) and k <= MAX:
        pxk = horner_method(p, x)
        pxk_d1 = horner_method(derivate_p(p), x)
        pxk_d2 = horner_method(derivate_p(derivate_p(p)), x)
        hxk = pow((n - 1) * pxk_d1, 2) - n * (n - 1) * pxk * pxk_d2
        if hxk < 0:
            break
        denominator = (pxk_d1 + sign(pxk_d1) * math.sqrt(hxk))
        if - EPS <= denominator <= EPS:
            break
        delta_xk = (n * pxk) / denominator
        x = x - delta_xk
        k = k + 1
    if abs(delta_xk) < EPS:
        return x
    else:
        return None


def write_solutions(p, solutions):
    f = open('solutions.txt', 'a')
    i = 0
    f.write(f"Polynom:{p}\n")
    for s in solutions:
        f.write(f'x{i} = {s}\n')
        i += 1
    f.write('\n')
    f.close()


def solve_polynom(p):
    solutions = set()
    r = get_interval(p)
    for i in range(iterations):
        x0 = random.uniform(-r, r)
        x = solve_laguerre(p, x0, r)
        if x is not None:
            solutions.add(round(x, 6))
    write_solutions(p, solutions)
    return solutions


if __name__ == '__main__':
    polynom = [6, 33, 6, -45]
    print(f"Interval [-{get_interval(polynom)}, {get_interval(polynom)}]")
    print(f"Solution for {polynom}: {solve_polynom(polynom)}")

    polynom = [1, 1, 1]
    print(f"Solution for {polynom}: {solve_polynom(polynom)}")
    print(f"Interval [-{get_interval(polynom)}, {get_interval(polynom)}]")

    polynom = [1, -6, 11, -6]
    print(f"Interval [-{get_interval(polynom)}, {get_interval(polynom)}]")
    print(f"Solution for {polynom}: {solve_polynom(polynom)}")

    polynom = [42, -55, -42, 49, -6]
    print(f"Interval [-{get_interval(polynom)}, {get_interval(polynom)}]")
    print(f"Solution for {polynom}: {solve_polynom(polynom)}")

    polynom = [8, -38, 49, -22, 3]
    print(f"Interval [-{get_interval(polynom)}, {get_interval(polynom)}]")
    print(f"Solution for {polynom}: {solve_polynom(polynom)}")

    polynom = [1, -6, 13, -12, 4]
    print(f"Interval [-{get_interval(polynom)}, {get_interval(polynom)}]")
    print(f"Solution for {polynom}: {solve_polynom(polynom)}")