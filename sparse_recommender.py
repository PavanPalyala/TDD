class SparseMatrix:
    def __init__(self):
        self.matrix = {}

    def set(self, row, col, value):
        if value != 0:
            self.matrix[(row, col)] = value

    def get(self, row, col):
        return self.matrix.get((row, col), 0)

    def recommend(self, vector):
        result = {}
        for (row, col), value in self.matrix.items():
            result[row] = result.get(row, 0) + value * vector[col]
        return result

    def add_movie(self, matrix):
        for (row, col), value in matrix.items():
            self.set(row, col, value)
        return self.matrix

    def to_dense(self):
        max_row = max(row for (row, _) in self.matrix.keys()) + 1
        max_col = max(col for (_, col) in self.matrix.keys()) + 1
        dense_matrix = [[0 for _ in range(max_col)] for _ in range(max_row)]
        for (row, col), value in self.matrix.items():
            dense_matrix[row][col] = value
        return dense_matrix