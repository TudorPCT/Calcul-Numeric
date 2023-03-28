import math
import random
import re

import numpy as np

from tema_4.RareMatrix import RareMatrix


def generate_sym_rare_matrix(n):
    a = RareMatrix(size=n)
    for i in range(n):
        for j in range(i, n):
            probability = 0.5
            if random.random() < probability:
                if a.matrix.get(i) is None:
                    a.matrix[i] = {}
                if a.matrix.get(j) is None:
                    a.matrix[j] = {}
                a.matrix[i][j] = random.uniform(0, 1000)
                a.matrix[j][i] = a.matrix[i][j]
    return a


def v_init(n):
    v = np.zeros(n)
    v[0] = random.uniform(0, 1 / n)
    norm = 1 - v[0] ** 2

    for i in range(n-1):
        v[i] = random.uniform(0, math.sqrt(norm))
        norm -= v[i] ** 2

    v[n-1] = math.sqrt(norm)

    return v


def power_iteration(a: RareMatrix):
    v = v_init(a.size)
    print(np.linalg.norm(v))
    print(v)
