import math

def execute_formula(formula_function, x):
    try:
        result = formula_function(x)
        print(f"Результат: y = {result:.6f}")
    except ValueError as error_msg:
        print(f"Помилка обчислення: {error_msg}")
    except ZeroDivisionError:
        print("Помилка: Відбулося ділення на нуль.")
    except Exception as e:
        print(f"Непередбачена помилка: {e}")



def formula_1(x):
    x = math.radians(x)
    print(f"Проміжне значення x в радіанах: {x:.6f}")
    sin_x = math.sin(x)
    log_arg = sin_x + 0.5
    
    if log_arg <= 0:
        raise ValueError(f"Аргумент логарифма (sin({x}°) + 0.5) дорівнює {log_arg:.4f}, що ≤ 0.")
        
    return math.log(log_arg)


def formula_2(x):
    x = math.radians(x)
    print(f"Проміжне значення x в радіанах: {x:.6f}")
    if x < -1 or x > 1:
        raise ValueError(f"Аргумент арксинуса (x={x}) виходить за межі допустимого діапазону [-1; 1].")
        
    arcsin_x = math.asin(x)
    root_arg = 1 - arcsin_x
    
    if root_arg < 0:
        raise ValueError("Підкореневий вираз (1 - arcsin(x)) є від'ємним.")
    if root_arg == 0:
        raise ValueError("Знаменник sqrt(1 - arcsin(x)) дорівнює нулю.")
    
    x_square = x**2
    sin_x_square = math.sin(math.radians(x_square))
    
    if sin_x_square == 0:
        raise ValueError("Знаменник котангенса (sin(x^2)) дорівнює нулю.")
        
    ctg = math.cos(math.radians(x_square)) / sin_x_square
    
    return ctg / math.sqrt(root_arg)


def main():
    stop_key = input("Введіть ключове значення, яке буде зупиняти програму: ")
    print(f"Програма працюватиме, поки ви не введете '{stop_key}'.\n")
    
    while True:
        user_input = input(f"\nВведіть аргумент x (або '{stop_key}' для виходу): ")
        
        if user_input == stop_key:
            print("Отримано ключове значення. Роботу програми завершено.")
            break
        
        try:
            x = float(user_input)
        except ValueError:
            print("Помилка: Будь ласка, введіть числове значення.")
            continue

        print("-" * 55)

        if x < 1:
            print("Функція: y = ln(sin(x) + 0.5)")
            execute_formula(formula_1, x)
            
        elif x > 10:
            print("Функція: y = ctg(x^2) / sqrt(1 - arcsin(x))")
            execute_formula(formula_2, x)
            
        else:
            print("Функція: Відсутня")
            print("Помилка: Функція не визначена на проміжку [1; 10].")
            continue

if __name__ == "__main__":
    main()