from tema_5.util import load_rare_matrix


class RareMatrixNew:
    def __init__(self, path=None, epsilon=10**-8, matrix=[], size=None):
        self.path = path
        self.epsilon = epsilon
        self.matrix, self.size = load_rare_matrix(self.path, epsilon) if size is None else (matrix, size)

    def is_symmetrical(self):
        for index, i in enumerate(self.matrix):
            for j in i:
                above_main_diagonal = j[0]

                for k in self.matrix[j[1]]:
                    if k[1] == index and abs(above_main_diagonal - k[0]) >= self.epsilon:
                        return False
        return True
