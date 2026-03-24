# def insert_element_custom(lst, value, index):
#     n = len(lst)

#     if index < 0:
#         index = n + index
#         if index < 0:
#             index = 0
#     if index > n:
#         index = n

#     result = []

#     for i in range(n):
#         if i == index:
#             result.append(value)
#         result.append(lst[i])

#     if index == n:
#         result.append(value)

#     return result

def insert_element(lst, value, index):
    return lst[:index] + [value] + lst[index:]

def main():
    try:
        user_input = input("Введіть елементи списку: ")
        lst = [int(x) for x in user_input.split()]
        
        val = int(input("Введіть число, яке треба вставити: "))
        idx = int(input("Введіть індекс, перед яким вставити: "))
        
        result = insert_element(lst, val, idx)
        
        print(f"Початковий список: {lst}")
        print(f"Оновлений список:   {result}")
        
    except ValueError:
        print("Помилка")

if __name__ == "__main__":
    main()