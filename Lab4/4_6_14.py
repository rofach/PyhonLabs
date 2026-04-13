import numpy as np

def create_matrix(n):
    matrix = np.zeros((7, 7), dtype=int)
    i, j = np.indices((7, 7))
    matrix[np.abs(i - 3) + np.abs(j - 3) == 3] = n
    return matrix

def main():
    N = 14
    
    result_matrix = create_matrix(N)
    
    print(result_matrix)

if __name__ == "__main__":
    main()