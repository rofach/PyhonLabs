def remove_element_generator(lst, n):
    return [x for x in lst if x != n]

def main():
    try:
        user_input = input("Введіть елементи списку: ")
        lst = [int(x) for x in user_input.split()]
        n = int(input("Введіть число n, яке потрібно видалити: "))
        
        result = remove_element_generator(lst, n)
        
        print(f"Початковий список: {lst}")
        print(f"Список без числа {n}: {result}")
    except ValueError:
        print("Помилка")

if __name__ == "__main__":
    main()