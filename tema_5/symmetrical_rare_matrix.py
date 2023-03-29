import math
import random
import re

import numpy as np

from tema_4.RareMatrix import RareMatrix


def generate_sym_rare_matrix(n):
    a = RareMatrix(size=n)
    probability = 2 / n
    count = 0

    for i in range(n):
        for j in range(i, n):
            if random.random() < probability:
                if a.matrix.get(i) is None:
                    a.matrix[i] = {}
                if a.matrix.get(j) is None:
                    a.matrix[j] = {}
                a.matrix[i][j] = random.uniform(0, 1000)
                a.matrix[j][i] = a.matrix[i][j]
                count += 1
    # print(count)
    return a


def v_init(n):

    v = np.random.rand(n, 1)
    v = v / np.linalg.norm(v)

    return v


def compute_w(a: RareMatrix, v):
    w = np.zeros((a.size, 1))

    for i in a.matrix:
        for j in a.matrix[i]:
            w[i] += a.matrix[i][j] * v[j][0]

    return w


def power_iteration(a: RareMatrix, epsilon=10**-9, kmax=1000000):

    if not a.is_symmetrical():
        raise Exception("Matrix is not symmetrical")

    v = v_init(a.size)
    w = compute_w(a, v)
    r = (w.T @ v)[0][0]
    k = 0
    while True:
        v = w / np.linalg.norm(w)
        w = compute_w(a, v)
        r = (w.T @ v)[0][0]
        k += 1

        if np.linalg.norm(w - r * v) <= a.size * epsilon or k > kmax:
            break

    if k > kmax:
        print("Max iterations reached")
    else:
        return r, v, k
