import re

import numpy as np

from tema_4.RareMatrix import RareMatrix
from tema_4.util import load_rare_matrix, load_vector


class GaussSeidelRareSystem:
    def __init__(self, a_path, b_path, max_iterations=10000, epsilon=10**-8):
        self.a = None
        self.b = None
        self.b_path = b_path
        self.size = 0
        self.solution = []
        self.epsilon = epsilon
        self.gauss_seidel_solvable = True
        self.gauss_seidel_iterations = 0
        self.max_iterations = max_iterations
        self.norm = 0
        self.load_a(a_path)
        self.load_b()

    def load_a(self, path):
        try:
            self.a = RareMatrix(path=path, epsilon=self.epsilon)
            self.size = self.a.size
        except Exception as e:
            print(e)
            self.gauss_seidel_solvable = False

    def load_b(self):
        self.b, b_size = load_vector(self.b_path)

        if self.size != b_size:
            raise Exception("Matrix and vector sizes don't match")

    def solve(self):
        if not self.gauss_seidel_solvable:
            raise Exception("System is not solvable")

        self.solution = np.zeros((self.size, 1))
        # self.solution = np.array([[1.0], [2.0], [3.0], [4.0], [5.0]])
        self.gauss_seidel_iterations = 0

        while True:
            err = 0

            for index, x in enumerate(self.solution):
                olx_x = x[0]

                x[0] = (self.b[index][0] -
                     sum([self.a.matrix[index][j] * self.solution[j]
                         for j in self.a.matrix[index] if j != index])) \
                    / self.a.matrix[index][index]

                err += abs(olx_x - x[0])

            self.gauss_seidel_iterations += 1

            if not (self.epsilon <= err <= 10 ** 8):
                break

            if self.gauss_seidel_iterations >= self.max_iterations:
                raise Exception("We reached the maximum number of iterations")

        if err < self.epsilon:
            self.norm = self.compute_norm()
        else:
            raise Exception("We reached divergent solution")

        return self.solution

    def compute_norm(self):
        return max([abs(sum([self.a.matrix[i][j] *
                             self.solution[j]
                             for j in self.a.matrix[i]]) -
                        self.b[i][0])
                    for i in self.a.matrix])


