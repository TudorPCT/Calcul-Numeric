import numpy as np
import warnings
warnings.filterwarnings("ignore", category=RuntimeWarning)


def is_valid(a, size, epsilon):

    pos_def = [np.linalg.det(a[:i + 1, :i + 1]) > 0 for i in range(size)]

    return np.allclose(a, a.T, epsilon) and np.all(pos_def)


def choleski_decomposition(a, n, epsilon):
    d = np.zeros(n)

    if not is_valid(a, n, epsilon):
        return None

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


def check_correctness(a_init, a, d):
    for p in range(len(a)):
        new_a_pp = d[p] + sum(d[k] * a[p][k] ** 2 for k in range(p))
        if abs(new_a_pp - a_init[p][p]) > 10 ** -5:
            return False
        for i in range(p + 1, len(a)):
            new_a_ip = a[i][p] * d[p] + sum(d[k] * a[i][k] * a[p][k] for k in range(p))
            if abs(new_a_ip - a_init[i][p]) > 10 ** -5:
                return False
    return True


if __name__ == '__main__':

    # Exercitiul 1
    input_a = np.array([[1, 2.5, 3], [2.5, 8.25, 15.5], [3, 15.5, 43]])
    input_a_init = input_a.copy()
    d = choleski_decomposition(input_a, len(input_a), 10 ** -5)
    print("New A:\n", input_a)
    print("D:", d)
    print("Correctness:", check_correctness(input_a_init, input_a, d))

    # Exercitiul 2
    print("det(A):", compute_det(d))

    # Exercitiul 3

    # Exercitiul 4

    # Exercitiul 5

    # Dimensiunea matricei peste 100 si Bonus

    size = 150
    input_a = np.random.uniform(0, 100, size=(size, size))

    input_a = input_a + input_a.T

    for x in range(size):
        input_a[x][x] = sum(input_a[x][j] if x != j else 0 for j in range(size)) + 1

    input_a_init = input_a.copy()

    d = choleski_decomposition(input_a, len(input_a), 10 ** -5)

    print("Correctness:", check_correctness(input_a_init, input_a, d))



