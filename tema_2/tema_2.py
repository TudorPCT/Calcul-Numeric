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

    return d


def compute_det(d):
    determinant = 1
    for i in range(len(d)):
        determinant *= d[i]
    return determinant


if __name__ == '__main__':
    size = 3
    a = np.random.uniform(0, 20, size=(size, size))
    a = a + a.T

    for x in range(size):
        a[x][x] = sum(a[x][j] if x != j else 0 for j in range(size)) + 1

    a_init = a.copy()

    d = choleski_decomposition(a, len(a), 10 ** -5)

    l = np.tril(a, -1)
    np.fill_diagonal(l, 1)
    new_a = np.matmul(np.matmul(l, np.diag(d)), l.T)
    print(np.allclose(a_init, new_a))



