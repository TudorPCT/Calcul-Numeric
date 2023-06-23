import random

import numpy as np

epsilon = complex(10 ** -9, 0)


def horner(a, x):
    n = len(a)
    d = 0

    for i in range(0, n+1):
        d = d * x + a.c[i]

    return d


def compute_p(a, x: complex):

    p = - 2 * x.real
    q = x.real ** 2 + x.imag ** 2

    b = a.c[0]
    bn = a.c[1] - p * b

    for i in range(2, len(a.c)):
        aux = a.c[i] - p * bn - q * b
        b = bn
        bn = aux

    return complex(b * x.real + bn + p * b, b * x.imag)


def laguerre(a, kmax=1000):
    n = len(a)
    r = (abs(a[0]) + max([abs(a[i]) for i in range(1, n)])) / abs(a[0])

    a = np.poly1d(a)

    x = complex(random.uniform(-r, r), random.uniform(-r, r))
    k = 0

    while True:
        p = compute_p(a, x)

        p_der = compute_p(np.polyder(a), x)

        p_der_2 = compute_p(np.polyder(a, 2), x)

        h = (n - 1) ** 2 * p_der ** 2 - n * (n - 1) * p * p_der_2

        if abs(p_der + np.sign(p_der) * np.sqrt(h)) < epsilon:
            return None

        delta_x = n * p / (p_der + np.sign(p_der) * np.sqrt(h))

        x = x - delta_x

        k += 1

        if 10 ** 8 < abs(delta_x) < epsilon or k > kmax:
            break

    if abs(delta_x) < epsilon:
        return x
    else:
        return None


def find_roots(a, kmax=1000, m_max=20, file_path=None):
    roots = []
    m = 0
    f = None

    try:
        f = open(file_path, 'w')
    except:
        pass

    while m < m_max:
        r = laguerre(a, kmax)

        if r is None:
            continue

        if not next((True for x in roots if abs(x - r) < epsilon), False):
            roots.append(r)
            if not abs(r.imag) < epsilon.real:
                roots.append(r.conjugate())

            if f is not None:
                f.write(str(r) + '\n')

        m += 1

    return roots


if __name__ == '__main__':

    # print("Polinomul 1")
    _a = np.array([1.0, -3.0, 0.0, 2.0, -1.0, 4.0])
    # print(compute_p(np.poly1d(_a), complex(3, 0)))

    _roots = find_roots(_a, m_max=100, file_path='./results/polinomul_1.txt')

    print("Coeficienti: ", _a)
    print("Radacini: ", _roots)
    print("Radacini librarie: ", np.roots(_a))

    # print("============================================")
    #
    # print("Polinomul 2")
    # _a = np.array([42.0, -55.0, -42.0, 49.0, -6.0])
    #
    # _roots = find_roots(_a, m_max=50, file_path='./results/polinomul_2.txt')
    #
    # print("Coeficienti: ", _a)
    # print("Radacini: ", _roots)
    # print("Radacini librarie: ", np.roots(_a))
    #
    # print("============================================")
    #
    # print("Polinomul 3")
    # _a = np.array([8.0, -38.0, 49.0, -22.0, 3.0])
    #
    # _roots = find_roots(_a, m_max=30, file_path='./results/polinomul_3.txt')
    #
    # print("Coeficienti: ", _a)
    # print("Radacini: ", _roots)
    # print("Radacini librarie: ", np.roots(_a))
    #
    # print("============================================")
    #
    # print("Polinomul 4")
    # _a = np.array([1.0, -6.0, 13.0, -12.0, 4.0])
    #
    # _roots = find_roots(_a, file_path='./results/polinomul_4.txt')
    #
    # print("Coeficienti: ", _a)
    # print("Radacini: ", _roots)
    # print("Radacini librarie: ", np.roots(_a))

    # print("============================================")
    #
    # print("Polinomul 5")
    # _a = np.array([1.0, 0.0, 1.0])
    # print(compute_p(np.poly1d(_a), complex(0, 1)))
    #
    # _roots = find_roots(_a, file_path='./results/polinomul_5.txt')
    #
    # print("Coeficienti: ", _a)
    # print("Radacini: ", _roots)
    # print("Radacini librarie: ", np.roots(_a))
