from tema_4.RareMatrix import RareMatrix
from tema_5.symmetrical_rare_matrix import generate_sym_rare_matrix, power_iteration

if __name__ == '__main__':

    m_512_generated = generate_sym_rare_matrix(5)

    m_512 = RareMatrix(path='./surse/m_rar_sim_2023_512.txt')
    m_1024 = RareMatrix(path='./surse/m_rar_sim_2023_1024.txt')
    m_2023 = RareMatrix(path='./surse/m_rar_sim_2023_2023.txt')

    print(m_512_generated)
    power_iteration(m_512_generated)

