def f(x):
    return 1 / x

def main():
    try:
        start = float(input("Введіть нижню границю: "))
        end = float(input("Введіть верхню границю: "))
        step = float(input("Введіть крок: "))

        result = []
        current_x = start
        
        while current_x <= end + 1e-10:
            try:
                y = f(current_x)
                arg = round(current_x, 10)
                arg = int(arg) if arg == int(arg) else arg
                val = int(y) if y == int(y) else y
                result.append([arg, val])
            except (ZeroDivisionError, ValueError):
                result.append([])
            
            current_x += step

        print(result)
        
    except ValueError:
        print("Помилка")

if __name__ == "__main__":
    main()