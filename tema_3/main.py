import math
from math import sqrt

import numpy as np
from numpy.linalg import inv

epsilon = 10 ** -9


def get_b(a, s):
    return a @ s


def householder(a, n, b):
    q = np.identity(n, dtype=np.float64)
    # u = np.zeros(n, dtype=np.float64)
    b_init = b.copy()
    a_init = a.copy()
    beta = 0
    k = 0
    for r in range(0, n - 1):
        sigma = 0
        for i in range(r, n):
            sigma = sigma + pow(a[i][r], 2)
        if sigma <= epsilon:
            break
        k = sqrt(sigma)
        if a[r][r] > 0:
            k = -k
        beta = sigma - k * a[r][r]

        u = np.zeros(n, dtype=np.float64)
        u[r] = a[r][r] - k
        for i in range(r + 1, n):
            u[i] = a[i][r]

        # A = Pr*A
        for j in range(r + 1, n):
            s = 0
            for i in range(r, n):
                s = s + u[i] * a[i][j]
            gamma = s / beta
            for i in range(r, n):
                a[i][j] = a[i][j] - gamma * u[i]
        a[r][r] = k
        for i in range(r + 1, n):
            a[i][r] = 0
        s = 0
        for i in range(r, n):
            s = s + u[i] * b[i]
        gamma = s / beta
        for i in range(r, n):
            b[i] = b[i] - gamma * u[i]

        for j in range(0, n):
            s = 0
            for i in range(r, n):
                s = s + u[i] * q[i][j]
            gamma = s / beta
            for i in range(r, n):
                q[i][j] = q[i][j] - gamma * u[i]

    return q.transpose(), a


def solve_system(a, b, n):
    print(a)
    print(b)
    x = np.zeros(len(a), dtype=np.float64)
    # for i in range(len(a)-1, -1, -1):
    #     x[i] = b[i] - sum(a[i][j] * x[j] for j in range(i))

    for i in range(n - 1, -1, -1):
        x[i] = (b[i] - sum(a[i][j] * x[j] for j in range(i + 1, n))) / a[i][i]

    return x.transpose()


def norm_check(a, b):
    norm_v = a - b
    norm = 0
    for i in norm_v:
        norm = norm + i*i
    norm = math.sqrt(norm)
    return np.alltrue(norm <= epsilon)


if __name__ == '__main__':
    input_a = np.array([[0, 0, 4], [1, 2, 3], [0, 1, 2]], dtype=np.float64)
    input_s = np.array([[3], [2], [1]], dtype=np.float64)
    input_b = get_b(input_a, input_s)
    b_init = np.copy(input_b)
    a_init = np.copy(input_a)
    # input_a = np.array([[60, -72, -43], [80, 154, -99], [75, 310, 140]], dtype=np.float64)
    # input_b = np.array([[60], [80], [75]], dtype=np.float64)
    print("Initial system:")
    print("A:\n", input_a)
    print("b:\n", input_b)
    print("s:\n", input_s)
    q, r = householder(input_a, 3, input_b)
    print("Q:\n", q)
    print("R:\n", r)

    # system solved with q and r calculated by our function
    x_householder = solve_system(r, q.transpose() @ b_init, 3)
    print(x_householder)

    # system solved with q and r calculated by python lib
    q_lib, r_lib = np.linalg.qr(a_init)
    print(q_lib)
    print(r_lib)
    xqr = solve_system(r_lib, q_lib.transpose() @ b_init, 3)
    print(xqr)

    print(norm_check(xqr, x_householder))
