import math

import numpy as np
import numpy.linalg
from numpy.linalg import inv

from tema_4.RareMatrix import RareMatrix
from symmetrical_rare_matrix import generate_sym_rare_matrix, power_iteration, power_iteration_new
from RareMatrixNew import RareMatrixNew


def compute_norm1(x, y):
    norms = np.sum(np.abs(x - y), axis=0)
    norm1 = np.max(norms)
    return norm1


def compute_norm2(x, y):
    norm2 = 0
    diff = x - y
    for _i in diff:
        norm2 = norm2 + _i * _i
    norm2 = math.sqrt(norm2)
    return norm2


if __name__ == '__main__':
    # # print("Exemplu video")
    # # m = RareMatrix(path='./surse/m_test.txt')
    # # result_1 = power_iteration(m)
    # # print("Lambda: ", result_1[0])
    # # # print("V: ", result_1[1])
    # # print("Nr iteratii: ", result_1[2])
    # #
    # print("----------------------------------------------------")
    #
    # print("Exemplu generat random")
    # m_512_generated = generate_sym_rare_matrix(600)
    # result_2 = power_iteration(m_512_generated)
    # print("Lambda: ", result_2[0])
    # # print("V: ", result_2[1])
    # print("Nr iteratii: ", result_2[2])
    #
    # print("----------------------------------------------------")
    #
    # print("Exemplu din fisier - 512")
    # m_512 = RareMatrix(path='./surse/m_rar_sim_2023_512.txt')
    # result_4 = power_iteration(m_512)
    # print("Lambda: ", result_4[0])
    # # print("V: ", result_4[1])
    # print("Nr iteratii: ", result_4[2])
    #
    # print("----------------------------------------------------")
    #
    # print("Exemplu din fisier - 1024")
    # m_1024 = RareMatrix(path='./surse/m_rar_sim_2023_1024.txt')
    # result_5 = power_iteration(m_1024)
    # print("Lambda: ", result_5[0])
    # # print("V: ", result_5[1])
    # print("Nr iteratii: ", result_5[2])
    #
    # print("----------------------------------------------------")
    #
    # print("Exemplu din fisier - 2023")
    # m_2023 = RareMatrix(path='./surse/m_rar_sim_2023_2023.txt')
    # result_6 = power_iteration(m_2023)
    # print("Lambda: ", result_6[0])
    # # print("V: ", result_6[1])
    # print("Nr iteratii: ", result_6[2])

    # print("----------------------------------------------------")
    #
    # classic_matrix = np.array([[1, 1], [1, 0], [0, 1]], dtype=float)
    # u, s, vh = numpy.linalg.svd(classic_matrix, full_matrices=True)
    # print("u:\n", u)
    # print("s:\n", s)
    # print("vh:\n", vh)
    # print("valori singulare:\n", s)
    #
    # # rang
    # print("rang-biblioteca:\n", np.linalg.matrix_rank(classic_matrix))
    # rang = len(s)
    # print("rang -SVD:\n", rang)
    #
    # # nr conditionare a matricei
    # print("nr conditionare a matricei-biblioteca:\n", np.linalg.cond(classic_matrix))
    # print("nr conditionare a matricei:\n", np.max(s) / np.min(s))
    #
    # # pseudoinversa Moore-Penrose a matricei A
    # si = np.zeros_like(classic_matrix, dtype=float)
    # for i in range(len(s)):
    #     si[i][i] = 1 / s[i]
    # si = si.T
    # print("si:\n", si)
    # ai = np.dot(np.dot(vh.T, si), u.T)
    # print("pseudo-inversa MP a lui a:\n", ai)
    #
    # # xi -solutia sistemului
    # b = np.array([[7], [8], [9]], dtype=float)
    # system_sol = np.dot(ai, b)
    # print("xi: ", system_sol)
    # print("Init: ", classic_matrix)
    # print("b: ", np.dot(classic_matrix, system_sol))
    # print("Norma: ", compute_norm2(b, classic_matrix @ system_sol))
    #
    # # matricea pseudo-inversa in sensul celor mai mici patrate
    # aj = inv(np.dot(classic_matrix.T, classic_matrix)) @ classic_matrix.T
    # print("matricea pseudo-inversa in sensul celor mai mici patrate;\n", aj)
    # print("Norma", compute_norm1(ai, aj))
    #
    # x, residuals, rank, s = np.linalg.lstsq(classic_matrix, b, rcond=None)
    # print("Numpy", x)

    print("----------------------------------------------------")

    print("Exemplu din fisier - 512")
    m_512_new = RareMatrixNew(path='./surse/m_rar_sim_2023_512.txt')
    print(m_512_new.is_symmetrical())
    result_4 = power_iteration_new(m_512_new)
    # result_4 = power_iteration(m_512)
    print("Lambda: ", result_4[0])
    # print("V: ", result_4[1])
    print("Nr iteratii: ", result_4[2])

    m_512 = RareMatrix(path='./surse/m_rar_sim_2023_512.txt')
    result_4 = power_iteration(m_512)
    print("Lambda: ", result_4[0])
    # print("V: ", result_4[1])
    print("Nr iteratii: ", result_4[2])