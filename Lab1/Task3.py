import math

def calc_with_for(n, x):
    current_val = 0.0
    
    for k in range(n, 0, -1):
        sum_k = k * (k + 1) / 2
        expr = sum_k + x + current_val
        
        if expr < 0:
            return False, 0.0
            
        current_val = math.sqrt(expr)
        
    return True, current_val

def calc_with_while(n, x):
    current_val = 0.0
    k = n
    
    while k > 0:
        sum_k = k * (k + 1) / 2
        expr = sum_k + x + current_val
        
        if expr < 0:
            return False, 0.0
            
        current_val = math.sqrt(expr)
        k -= 1
        
    return True, current_val

def calc_with_recursion(n, x, k=1):
    if k > n:
        return True, 0.0
        
    success, val = calc_with_recursion(n, x, k + 1)
    
    if not success:
        return False, 0.0
        
    sum_k = k * (k + 1) / 2
    expr = sum_k + x + val
    
    if expr < 0:
        return False, 0.0
        
    return True, math.sqrt(expr)

def main():
    try:
        n = int(input("Введіть кількість коренів n: "))
        if n < 1:
            print("Помилка: n має бути більшим або дорівнювати 1.")
            return
            
        x = float(input("Введіть дійсне число x: "))
    except ValueError:
        print("Помилка: Будь ласка, введіть коректні числові значення.")
        return

    print("-" * 50)
    
    success_for, res_for = calc_with_for(n, x)
    if success_for:
        print(f"Результат (FOR):       {res_for:.6f}")
    else:
        print("Результат (FOR):       Помилка (від'ємне число під коренем)")

    success_while, res_while = calc_with_while(n, x)
    if success_while:
        print(f"Результат (WHILE):     {res_while:.6f}")
    else:
        print("Результат (WHILE):     Помилка (від'ємне число під коренем)")

    success_rec, res_rec = calc_with_recursion(n, x)
    if success_rec:
        print(f"Результат (РЕКУРСІЯ):  {res_rec:.6f}")
    else:
        print("Результат (РЕКУРСІЯ):  Помилка (від'ємне число під коренем)")

if __name__ == "__main__":
    main()