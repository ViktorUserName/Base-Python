import random


def matrix_create(m, n, low=0, high=10):
    matrix = []

    for i in range(m):
        row = [random.randint(low, high) for _ in range(n)]
        matrix.append(row)

    return matrix

print(matrix_create(2,3))