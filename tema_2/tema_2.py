import numpy
import numpy as np


def choleski_decomposition(a, n, epsilon):
    d = np.zeros(n)

    for p in range(n):
        d[p] = a[p][p] - sum(d[k] * a[p][k] ** 2 for k in range(p))

        if abs(d[p]) < epsilon:
            return None

        for i in range(p + 1, n):
            a[i][p] = (a[i][p] - sum(d[k] * a[i][k] * a[p][k] for k in range(p))) / d[p]

    return a, d


def compute_determinant(d):
    determinant = 1
    for i in range(len(d)):
        determinant *= d[i][i]
    return determinant


if __name__ == '__main__':
    input_a = [[1, 2.5, 3], [2.5, 8.25, 15.5], [3, 15.5, 43]]
    input_a, input_d = choleski_decomposition(np.array(input_a), 3, 0.0001)

