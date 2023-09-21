import pytest
from sparse_recommender import SparseMatrix

def test_set_and_get():
    matrix = SparseMatrix()
    matrix.set(0, 0, 1)
    assert matrix.get(0, 0) == 1

def test_recommend():
    matrix = SparseMatrix()
    matrix.set(0, 0, 1)
    matrix.set(1, 1, 2)
    vector = [1, 2]
    result = matrix.recommend(vector)
    assert result == {0: 1, 1: 4}

def test_add_movie():
    matrix1 = SparseMatrix()
    matrix1.set(0, 0, 1)
    matrix1.set(1, 1, 2)
    
    matrix2 = SparseMatrix()
    matrix2.set(0, 1, 3)
    matrix2.set(1, 0, 4)
    
    result = matrix1.add_movie(matrix2)
    assert result == {(0, 0): 1, (1, 1): 2, (0, 1): 3, (1, 0): 4}

def test_to_dense():
    matrix = SparseMatrix()
    matrix.set(0, 0, 1)
    matrix.set(1, 1, 2)
    dense_matrix = matrix.to_dense()
    assert dense_matrix == [[1, 0], [0, 2]]

def test_default_value():
    matrix = SparseMatrix()
    assert matrix.get(0, 0) == 0

if __name__ == "__main__":
    pytest.main()
