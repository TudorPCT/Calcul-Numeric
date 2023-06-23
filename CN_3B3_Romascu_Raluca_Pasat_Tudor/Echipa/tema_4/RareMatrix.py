from tema_4.util import load_rare_matrix


class RareMatrix:
    def __init__(self, path=None, epsilon=10**-8, matrix={}, size=None):
        self.path = path
        self.epsilon = epsilon
        self.matrix, self.size = load_rare_matrix(self.path, epsilon) if size is None else (matrix, size)

    def sum(self, b: "RareMatrix"):

        if self.size != b.size:
            raise Exception("Vector sizes don't match")

        result = {}

        for i in self.matrix:
            for j in self.matrix[i]:
                if result.get(i) is None:
                    result[i] = {}
                result[i][j] = self.matrix[i][j] + b.matrix.get(i, {}).get(j, 0)

        for i in b.matrix:
            for j in b.matrix[i]:
                if result.get(i) is None:
                    result[i] = {}
                if result[i].get(j) is None:
                    result[i][j] = b.matrix[i][j]

        return RareMatrix(matrix=result, size=self.size)

    def equals(self, b):
        if type(b) is not RareMatrix:
            return False

        for i in self.matrix:
            for j in self.matrix[i]:
                if abs(self.matrix[i][j] - b.matrix.get(i, {}).get(j, 0)) >= self.epsilon:
                    return False
        return True

    def __str__(self):
        return str(self.matrix)

    def is_symmetrical(self):
        for i in self.matrix:
            for j in self.matrix[i]:
                above_main_diagonal = self.matrix.get(i, {}).get(j, 0)
                below_main_diagonal = self.matrix.get(j, {}).get(i, 0)
                if abs(above_main_diagonal - below_main_diagonal) >= self.epsilon:
                    return False
        return True
