import numpy as np

def create_antidiagonal_matrix(k, n):
    matrix = np.zeros((k, k), dtype=int)
    i = np.arange(k)
    matrix[i, k - 1 - i] = n
    return matrix

def main():
    K = int(input("K: "))
    N = 14
    
    result_matrix = create_antidiagonal_matrix(K, N)
    
    print(result_matrix)


main()

    