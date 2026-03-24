import random

def fill_list_with_randoms(n, a, b):
    return [random.randint(a, b) for _ in range(n)]

def main():
    try:
        n = int(input("Введіть кількість елементів: "))
        a = int(input("Введіть початок інтервалу: "))
        b = int(input("Введіть кінець інтервалу: "))

        result = fill_list_with_randoms(n, a, b)
        print(f"Список: {result}")
    except ValueError:
        print("Помилка")

if __name__ == "__main__":
    main()