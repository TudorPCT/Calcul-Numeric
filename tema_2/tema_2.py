import numpy as np
import scipy.linalg
import warnings

warnings.filterwarnings("ignore", category=RuntimeWarning)


def choleski_decomposition(a, n, epsilon):
    d = np.zeros(n, dtype=np.float64)

    if not (len(a) == len(a[0]) == n or np.allclose(a, a.T, epsilon)):
        return None

    for p in range(n):

        d[p] = a[p][p] - sum(d[k] * a[p][k] ** 2 for k in range(p))

        if abs(d[p]) < epsilon and abs(np.linalg.det(a[:p + 1, :p + 1])) <= epsilon:
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


def solve_system(a, b, d, epsilon):
    if not (len(a) == len(a[0]) == len(b) == len(d) or abs(compute_det(b)) < epsilon):
        return None

    x = np.zeros(len(a), dtype=np.float64)
    for i in range(len(a)):
        x[i] = b[i] - sum(a[i][j] * x[j] for j in range(i))

    for i in range(len(a)):
        x[i] /= d[i]

    for i in range(len(a) - 1, -1, -1):
        x[i] = x[i] - sum(a[j][i] * x[j] for j in range(i + 1, len(a)))

    return x.T


def lu_decomposition(a, n, epsilon):
    if not (len(a) == len(a[0]) == n or np.allclose(a, a.T, epsilon)):
        return None
    _p, _l, _u = scipy.linalg.lu(a)
    return _p, _l, _u


def lu_correctness(a, l, u):
    if np.allclose(a, l @ u, rtol=pow(10, -5), atol=pow(10, -9)):
        return True
    return False


def lu_solution(a, b):
    _p, _l, _u = scipy.linalg.lu(a)
    y = scipy.linalg.solve_triangular(_l, _p.dot(b), lower=True)
    x = scipy.linalg.solve_triangular(_u, y)
    return x


def norm_check(a, b, x):
    x = x.transpose()
    norm_v = a @ x - b
    norm = 0
    for i in norm_v:
        norm = norm + i*i

    return np.alltrue(norm <= pow(10, -9))


if __name__ == '__main__':
    # Exercitiul 1
    # input_a = np.array([[1, 2.5, 3], [2.5, 8.25, 15.5], [3, 15.5, 43]])
    input_a = np.array([[1, 3, 6], [3, 13, 28], [6, 28, 77]], dtype=np.float64)
    input_b = np.array([3, 13, 28], dtype=np.float64)

    input_a_init = input_a.copy()
    _m = 9

    _d = choleski_decomposition(input_a, len(input_a), 10 ** -_m)

    print("New A:\n", input_a)
    print("D:", _d)
    print("Correctness:", check_correctness(input_a_init, input_a, _d))

    # Exercitiul 2
    print("det(A):", compute_det(_d))

    # Exercitiul 3
    print("x:", solve_system(input_a, input_b, _d, 10 ** -_m))

    # Exercitiul 4
    input_a = np.array([[1, 2.5, 3], [2.5, 8.25, 15.5], [3, 15.5, 43]], dtype=np.float64)
    input_b = np.array([12, 38, 68], dtype=np.float64)
    input_a_init = input_a.copy()
    _m = 9

    p, l, u = lu_decomposition(input_a, len(input_a), 10 ** -_m)
    print("A init:\n", input_a_init)
    print("L:\n", p @ l)
    print("U:\n", u)
    print("Correctness:", lu_correctness(input_a_init, p @ l, u))

    print("x:", lu_solution(input_a, input_b))

    # Exercitiul 5
    print("Euclidean Norm: ", norm_check(input_a_init, input_b,
                                         solve_system(input_a, input_b,
                                                      choleski_decomposition(input_a, len(input_a), 10 ** -_m),
                                                      10 ** -_m)))

    # Dimensiunea matricei peste 100 si Bonus

    size = 150
    input_a = np.random.uniform(0, 100, size=(size, size))

    input_a = input_a + input_a.T

    for _x in range(size):
        input_a[_x][_x] = sum(abs(input_a[_x][_y]) if _x != _y else 0 for _y in range(size)) + 1

    input_a_init = input_a.copy()
    input_b = np.random.uniform(0, 100, size=size)

    _d = choleski_decomposition(input_a, len(input_a), 10 ** -_m)

    print("Correctness for size = 150:", check_correctness(input_a_init, input_a, _d))
    print("Euclidean Norm: ", norm_check(input_a_init, input_b, solve_system(input_a, input_b, _d, 10 ** -_m)))




