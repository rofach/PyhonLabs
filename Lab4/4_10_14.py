import numpy as np
import matplotlib.pyplot as plt

def calc(x):
    y = np.full_like(x, np.nan, dtype=float)
    
    with np.errstate(invalid='ignore', divide='ignore'):
        mask1 = (x > -1) & (x < 3)
        y[mask1] = np.sqrt(np.log(x[mask1]) / np.tan(x[mask1]**2))
        
        mask2 = x > 4
        y[mask2] = np.cos(np.log(x[mask2] - 5)) / (2 * np.sin(x[mask2]) - 1)
        
    return y

def main():
    x = np.linspace(-1, 15, 00)
    
    y = calc(x)
    
    plt.figure(figsize=(5, 5))
    plt.plot(x, y, color='b', linewidth=2)
    
    plt.title("Графік")
    plt.xlabel("x")
    plt.ylabel("y")
    plt.grid(True)
    plt.axhline(0, color='black', linewidth=0.5)
    plt.axvline(0, color='black', linewidth=0.5)
    
    plt.ylim(-10, 10)
    
    plt.show()

main()