import numpy as np
import numpy.linalg

from tema_4.RareMatrix import RareMatrix
from symmetrical_rare_matrix import generate_sym_rare_matrix, power_iteration

if __name__ == '__main__':
    # print("Exemplu video")
    # m = RareMatrix(path='./surse/m_test.txt')
    # result_1 = power_iteration(m)
    # print("Lambda: ", result_1[0])
    # # print("V: ", result_1[1])
    # print("Nr iteratii: ", result_1[2])
    #
    # print("----------------------------------------------------")
    #
    # print("Exemplu generat random")
    # m_512_generated = generate_sym_rare_matrix(700)
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

    print("----------------------------------------------------")

    # print("Exemplu din fisier - 2023")
    # m_2023 = RareMatrix(path='./surse/m_rar_sim_2023_2023.txt')
    # result_6 = power_iteration(m_2023)
    # print("Lambda: ", result_6[0])
    # # print("V: ", result_6[1])
    # print("Nr iteratii: ", result_6[2])

    print("----------------------------------------------------")

    classic_matrix = np.array([[1, 1], [1, 0], [0, 1]], dtype=float)
    u, s, vh = numpy.linalg.svd(classic_matrix, full_matrices=True)
    print("u:\n", u)
    print("s:\n", s)
    print("vh:\n", vh)
    print("valori singulare:\n", s)
    print("rang A:\n", len(s))
    print("nr conditionare a matricei:\n", np.max(s) / np.min(s))
    # si = np.zeros_like(classic_matrix, dtype=float)
    # print(s.shape)
    # print(si)
    # si[:min(classic_matrix.shape)] = 1 / s[:min(classic_matrix.shape)]
    # print(si)
    # si = si.T
    # print(si)
    # ai = vh.T @ si @ u.T
    # print("pseudo-inversa MP a lui a:\n", ai)
