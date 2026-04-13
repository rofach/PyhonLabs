import numpy as np
import matplotlib.pyplot as plt

def normalize_array(arr):
    x_min = np.min(arr)
    x_max = np.max(arr)
    
    if x_max == x_min:
        return np.zeros_like(arr)
    
    return (arr - x_min) / (x_max - x_min)

def main():
    K = int(input("K: "))
    L = float(input("L: "))
    N = float(input("N: "))
    
    original_array = np.random.uniform(L, N, K)
    
    normalized_array = normalize_array(original_array)
    
    print("Початковий масив:")
    print(original_array)
    print("\nНормалізований масив:")
    print(normalized_array)
    
    fig, (ax1, ax2) = plt.subplots(1, 2, figsize=(12, 5))
    
    ax1.bar(range(K), original_array)
    ax1.set_title("Початковий масив")
    
    ax2.bar(range(K), normalized_array)
    ax2.set_title("Нормалізований масив")
    
    plt.show()

main()