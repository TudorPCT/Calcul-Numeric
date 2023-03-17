import math
from math import sqrt

import numpy as np
from numpy.linalg import inv

epsilon = 10 ** -9


def get_b(a, s):
    # b = np.zeros(len(a), dtype=np.float64)
    # for i in range(len(a)):
    #     for j in range(len(a)):
    #         b[i] = b[i] + a[i][j] * s[j]
    return a @ s


def householder(a, n, b):
    q = np.identity(n, dtype=np.float64)
    for r in range(0, n - 1):
        sigma = 0
        for i in range(r, n):
            sigma = sigma + pow(a[i][r], 2)
        if sigma <= epsilon:
            return None

        k = sqrt(sigma)
        if a[r][r] >= 0:
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

        # b = Pr*b
        s = 0
        for i in range(r, n):
            s = s + u[i] * b[i]
        gamma = s / beta
        for i in range(r, n):
            b[i] = b[i] - gamma * u[i]

        # Q = Q*Pr
        for j in range(0, n):
            s = 0
            for i in range(r, n):
                s = s + u[i] * q[i][j]
            gamma = s / beta
            for i in range(r, n):
                q[i][j] = q[i][j] - gamma * u[i]

    return q.transpose()


def solve_system(a, b, n):
    # print(a)
    # print(b)
    x = np.zeros(len(a), dtype=np.float64)

    for i in range(n - 1, -1, -1):
        x[i] = (b[i] - sum(a[i][j] * x[j] for j in range(i + 1, n))) / a[i][i]

    return x.transpose()


def solve_householder(a, s):
    b = get_b(a, s)
    _ = householder(a, len(a), b)
    return solve_system(a, b, len(a))


def compute_norm(norm_v):
    norm = 0
    for i in norm_v:
        norm = norm + i * i
    norm = math.sqrt(norm)
    return norm


def compute_inv(a):
    a_inv = np.empty((len(a), 0), dtype=np.float64)
    _a = np.copy(a)
    q = householder(_a, len(_a), get_b(_a, np.identity(len(_a), dtype=np.float64)))
    if np.alltrue(abs(np.diag(_a)) < epsilon):
        print("Matrix is singular")
        return None

    for j in range(len(a)):
        b = q[j]
        x = solve_system(_a, b, len(a))
        a_inv = np.column_stack((a_inv, x))

    return a_inv


def build_a_k_1(a_k, a_k_1, b):
    n = len(a_k)
    q = householder(a_k, len(a_k), b)

    for i in range(n):
        for j in range(n):
            a_k_1[i][j] = sum(a_k[i][k] * q[k][j] for k in range(i, n))
            a_k_1[j][i] = a_k_1[i][j]


def compute_limit(a_k):
    b = np.zeros(len(a_k), dtype=np.float64)
    aux = np.zeros((len(a_k), len(a_k)), dtype=np.float64)
    a_k_1 = np.zeros((len(a_k), len(a_k)), dtype=np.float64)
    while True:
        np.copyto(aux, a_k)
        build_a_k_1(aux, a_k_1, b)

        norm = np.linalg.norm(a_k_1 - a_k)
        if norm <= epsilon:
            return a_k_1
        a_k, a_k_1 = a_k_1, a_k


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
    print("=====================================")
    print("Exercise 1")
    print("b:\n", input_b)
    print("=====================================")
    print("s:\n", input_s)

    print("=====================================")
    print("Exercise 2")
    _q = householder(input_a, 3, input_b)
    print("Q:\n", _q)
    print("R:\n", input_a)
    print("=====================================")

    print("Exercise 3")
    # system solved with q and r calculated by our function
    x_householder = solve_householder(a_init.copy(), input_s)
    print("X: ", x_householder)

    # system solved with q and r calculated by python lib
    q_lib, r_lib = np.linalg.qr(a_init)
    print("Q lib\n", q_lib)
    print("R lib\n", r_lib)
    xqr = solve_system(r_lib, q_lib.transpose() @ b_init, 3)
    print("XQR lib", xqr)

    print("Norm3: ", compute_norm(x_householder - xqr))
    print("=====================================")

    print("Exercise 4")
    print("Norm41:", compute_norm(a_init @ x_householder - b_init.T[0]))
    print("Norm42:", compute_norm(a_init @ xqr - b_init.T[0]))
    print("Norm43:", compute_norm(x_householder - input_s.T[0]) / compute_norm(input_s.T[0]))
    print("Norm44:", compute_norm(xqr - input_s.T[0]) / compute_norm(input_s.T[0]))

    print("=====================================")
    print("Exercise 5")
    _a_inv = compute_inv(a_init)
    print("Inverse of A:\n", _a_inv)
    a_inv_lib = np.linalg.inv(a_init)
    print("Inverse of A lib:\n", a_inv_lib)
    print("Norm5:", np.linalg.norm(_a_inv - a_inv_lib))

    print("=====================================")
    print("Exercise 6")
    size = 150
    input_a_n = np.random.uniform(0, 100, size=(size, size))
    input_s_n = np.random.uniform(0, 100, size=(size, 1))
    input_b_n = get_b(input_a_n, input_s_n)

    q_lib_n, r_lib_n = np.linalg.qr(input_a_n)
    xqr_n = solve_system(r_lib_n, q_lib_n.transpose() @ input_b_n, len(input_a_n))
    x_householder_n = solve_householder(input_a_n.copy(), input_s_n)

    # print("X: ", x_householder_n)
    # print("XQR: ", x_qr_n)
    print("Norm6: ", compute_norm(x_householder_n - xqr_n) < 10 ** -6)
    print("=====================================")
    print("Bonus")

    size = 3
    input_a = np.array([[0, 0, 4], [1, 2, 3], [0, 1, 2]], dtype=np.float64)

    input_a = input_a + input_a.T

    input_a_init = input_a.copy()
    input_b = input_a, np.identity(size, dtype=np.float64)

    limit = compute_limit(input_a)
    print("Limit:\n", limit)
