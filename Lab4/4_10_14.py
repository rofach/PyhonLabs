import numpy as np
import matplotlib.pyplot as plt

def calc(x):
    y = np.full_like(x, np.nan, dtype=float)
    
    np.errstate(invalid='ignore', divide='ignore')
    cond1 = (x > -1) & (x < 3)
    y[cond1] = np.sqrt(np.log(x[cond1]) / np.tan(x[cond1]**2))
        
    cond2 = x > 4
    y[cond2] = np.cos(np.log(x[cond2] - 5)) / (2 * np.sin(x[cond2]) - 1)
        
    return y

def main():
    x = np.linspace(-15, 15, 2000)
    
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