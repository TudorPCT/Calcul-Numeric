def compute_p_1(a, b, n, n_min):
    return multiply_strassen(
            [[a[i][j] + a[i + n // 2][j + n // 2] for j in range(n // 2)] for i in range(n // 2)],
            [[b[i][j] + b[i + n // 2][j + n // 2] for j in range(n // 2)] for i in range(n // 2)],
            n // 2,
            n_min
    )


def compute_p_2(a, b, n, n_min):
    return multiply_strassen(
            [[a[i + n // 2][j] + a[i + n // 2][j + n // 2] for j in range(n // 2)] for i in range(n // 2)],
            [[b[i][j] for j in range(n // 2)] for i in range(n // 2)],
            n // 2,
            n_min
    )


def compute_p_3(a, b, n, n_min):
    return multiply_strassen(
            [[a[i][j] for j in range(n // 2)] for i in range(n // 2)],
            [[b[i][j + n // 2] - b[i + n // 2][j + n // 2] for j in range(n // 2)] for i in range(n // 2)],
            n // 2,
            n_min
    )


def compute_p_4(a, b, n, n_min):
    return multiply_strassen(
            [[a[i + n // 2][j + n // 2] for j in range(n // 2)] for i in range(n // 2)],
            [[b[i + n // 2][j] - b[i][j] for j in range(n // 2)] for i in range(n // 2)],
            n // 2,
            n_min
    )


def compute_p_5(a, b, n, n_min):
    return multiply_strassen(
            [[a[i][j] + a[i][j + n // 2] for j in range(n // 2)] for i in range(n // 2)],
            [[b[i + n // 2][j + n // 2] for j in range(n // 2)] for i in range(n // 2)],
            n // 2,
            n_min
    )


def compute_p_6(a, b, n, n_min):
    return multiply_strassen(
            [[a[i + n // 2][j] - a[i][j] for j in range(n // 2)] for i in range(n // 2)],
            [[b[i][j] + b[i][j + n // 2] for j in range(n // 2)] for i in range(n // 2)],
            n // 2,
            n_min
    )


def compute_p_7(a, b, n, n_min):
    return multiply_strassen(
            [[a[i][j + n // 2] - a[i + n // 2][j + n // 2] for j in range(n // 2)] for i in range(n // 2)],
            [[b[i + n // 2][j] + b[i + n // 2][j + n // 2] for j in range(n // 2)] for i in range(n // 2)],
            n // 2,
            n_min
    )


def compute_p(a, b, n, n_min):
    return compute_p_1(a, b, n, n_min),\
          compute_p_2(a, b, n, n_min), \
          compute_p_3(a, b, n, n_min),\
          compute_p_4(a, b, n, n_min),\
          compute_p_5(a, b, n, n_min), \
          compute_p_6(a, b, n, n_min), \
          compute_p_7(a, b, n, n_min)


def compute_c(p_1, p_2, p_3, p_4, p_5, p_6, p_7, n):
    c = [[0 for _ in range(n)] for _ in range(n)]
    for i in range(n // 2):
        for j in range(n // 2):
            c[i][j] = p_1[i][j] + p_4[i][j] - p_5[i][j] + p_7[i][j]
            c[i][j + n // 2] = p_3[i][j] + p_5[i][j]
            c[i + n // 2][j] = p_2[i][j] + p_4[i][j]
            c[i + n // 2][j + n // 2] = p_1[i][j] - p_2[i][j] + p_3[i][j] + p_6[i][j]
    return c


def compute_exponent(number, divisor):
    exponent = 0
    while divisor ** exponent <= number:
        if divisor ** exponent == number:
            return exponent
        exponent += 1
    return exponent


def multiply_strassen(a, b, n, n_min):
    new_n = 2 ** compute_exponent(n, 2)

    padding = [0 for _ in range(new_n - n)]
    for i in range(n):
        a[i].extend(padding)
        b[i].extend(padding)

    padding = [[0 for _ in range(new_n)] for _ in range(new_n - n)]
    a.extend(padding)
    b.extend(padding)

    if new_n <= n_min:
        return [[sum(a[i][k] * b[k][j] for k in range(n)) for j in range(n)] for i in range(n)]
    else:
        p_1, p_2, p_3, p_4, p_5, p_6, p_7 = compute_p(a, b, new_n, n_min)
        c = compute_c(p_1, p_2, p_3, p_4, p_5, p_6, p_7, new_n)
        c = [row[:n] for row in c[:n]]
        return c
