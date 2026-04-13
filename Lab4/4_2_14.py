import numpy as np

def create_custom_matrix(m, n):
    matrix = np.full((m, n), 0.5)
    np.fill_diagonal(matrix, -1.0)
    
    return matrix

def get_submatrix(matrix, top_left, bottom_right):
    row_start = top_left[0]
    row_end = bottom_right[0] + 1
    col_start = top_left[1]
    col_end = bottom_right[1] + 1
    return matrix[row_start:row_end, col_start:col_end]

def main():
    M = int(input("M: "))
    N = int(input("N: "))
    matrix = create_custom_matrix(M, N)
    
    print("Початкова матриця:")
    print(matrix)
    top_left = [int(x) for x in input("верхній лівий кут: ").split()]
    bottom_right = [int(x) for x in input("нижній правий кут: ").split()]

    submatrix = get_submatrix(matrix, top_left, bottom_right)
    
    print("Виділена підматриця:")
    print(submatrix)


main()