import numpy as np

def create_checkerboard_matrix(k, n):
    matrix = np.zeros((k, k), dtype=int)
    
    i, j = np.indices((k, k))
    matrix[((i + j) % 2) == 1] = n
    return matrix

def main():
    K = int(input("K: "))
    N = 14
    
    result_matrix = create_checkerboard_matrix(K, N)
    
    print(result_matrix)


main()