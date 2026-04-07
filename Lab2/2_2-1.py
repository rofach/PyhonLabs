def filter_negatives(a):
    second_list = []
    for x in a:
        if x < 0:
            second_list.append(x)
    return second_list

def main():
    try:
        user_input = input("Введіть числа: ")
        a = [int(x) for x in user_input.split()]
        
        result = filter_negatives(a)
        
        print(f"Ваш список: {a}")
        print(f"Від'ємні числа: {result}")
    except ValueError:
        print("Помилка")

if __name__ == "__main__":
    main()