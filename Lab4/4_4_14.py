import numpy as np

def main():
    arr = np.array([float(x) for x in input("Введіть елементи: ").split()])
    n = float(input("Введіть значення: "))
    
    greater_elements = arr[arr > n]
    less_elements = arr[arr < n]
    
    print("Більші елементи:")
    print(greater_elements)
    
    print("Менші елементи:")
    print(less_elements)


main()