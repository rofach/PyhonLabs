import numpy as np

def main():
    arr = np.array([float(x) for x in input("Введіть елементи: ").split()])
    indices_array = np.array([int(x) for x in input("Введіть індекси: ").split()])
    
    result = arr[indices_array]
    
    print(result)


main()