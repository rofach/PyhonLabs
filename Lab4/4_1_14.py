import numpy as np

def create_custom_matrix(m, n):
    matrix = np.full((m, n), 0.5)
    
    np.fill_diagonal(matrix, -1.0)
    
    return matrix



def main():
    M = int(input("M: "))
    N = int(input("N: "))
    result = create_custom_matrix(M, N)
    print(result)

main()