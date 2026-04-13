import numpy as np

def smooth_image(k, l):
    matrix = np.random.randint(0, 256, size=(k, l))
    
    smoothed = matrix.copy()
    
    matrix1 = matrix[:-2, :-2]
    matrix2 = matrix[:-2, 1:-1]
    matrix3 = matrix[:-2, 2:]
    matrix4 = matrix[1:-1, :-2]
    matrix5 = matrix[1:-1, 1:-1]
    matrix6 = matrix[1:-1, 2:]
    matrix7 = matrix[2:, :-2]
    matrix8 = matrix[2:, 1:-1]
    matrix9 = matrix[2:, 2:]

    smoothed[1:-1, 1:-1] = (matrix1 + matrix2 + matrix3 + matrix4 + matrix5 + matrix6 + matrix7 + matrix8 + matrix9) // 9
    
    return matrix, smoothed

def main():
    K = int(input("K: "))
    L = int(input("L: "))
    
    original_matrix, smoothed_matrix = smooth_image(K, L)
    
    print("Початкова матриця:")
    print(original_matrix)
    
    print("\nЗгладжена матриця:")
    print(smoothed_matrix)

main()