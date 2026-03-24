def main():
    groups = {
        "КС-22": [25, "Староста 1"],
        "КС-21": [18, "Староста 2"],
        "КС-20": [30, "Староста 3"]
    }

    while True:
        print("\n--- МЕНЮ ---")
        print("1. Кількість студентів у групі")
        print("2. ПІБ старости групи")
        print("3. Групи, де студентів не більше заданого")
        print("4. Групи, де студентів не менше заданого")
        print("5. Змінити кількість студентів")
        print("6. Змінити ПІБ старости")
        print("7. Додати нову групу")
        print("8. Видалити групу")
        print("9. Множина ПІБ старост обраних груп")
        print("10. Вихід")

        choice = input("\nОберіть пункт меню: ")

        if choice == '1':
            name = input("Введіть назву групи: ")
            if name in groups:
                print(f"У групі {name} навчається {groups[name][0]} студентів.")
            else:
                print("Групу не знайдено.")

        elif choice == '2':
            name = input("Введіть назву групи: ")
            if name in groups:
                print(f"Староста групи {name}: {groups[name][1]}")
            else:
                print("Групу не знайдено.")

        elif choice == '3':
            try:
                limit = int(input("Введіть максимальну кількість: "))
                result = tuple(name for name, data in groups.items() if data[0] <= limit)
                print(f"Групи з кількістю <= {limit}: {result}")
            except ValueError:
                print("Помилка: введіть число.")

        elif choice == '4':
            try:
                limit = int(input("Введіть мінімальну кількість: "))
                result = tuple(name for name, data in groups.items() if data[0] >= limit)
                print(f"Групи з кількістю >= {limit}: {result}")
            except ValueError:
                print("Помилка: введіть число.")

        elif choice == '5':
            name = input("Введіть назву групи: ")
            if name in groups:
                try:
                    new_count = int(input("Введіть нову кількість студентів: "))
                    groups[name][0] = new_count
                    print("Дані оновлено.")
                except ValueError:
                    print("Помилка")
            else:
                print("Групу не знайдено.")

        elif choice == '6':
            name = input("Введіть назву групи: ")
            if name in groups:
                new_leader = input("Введіть нове ПІБ старости: ")
                groups[name][1] = new_leader
                print("Дані оновлено.")
            else:
                print("Групу не знайдено.")

        elif choice == '7':
            name = input("Назва нової групи: ")
            if name not in groups:
                try:
                    count = int(input("Кількість студентів: "))
                    leader = input("ПІБ старости: ")
                    groups[name] = [count, leader]
                    print(f"Групу {name} додано.")
                except ValueError:
                    print("Помилка при введенні числа.")
            else:
                print("Така група вже існує.")

        elif choice == '8':
            name = input("Введіть назву групи для видалення: ")
            if groups.pop(name, None):
                print(f"Групу {name} видалено.")
            else:
                print("Групу не знайдено.")

        elif choice == '9':
            names_input = input("Введіть назви груп: ").split()
            leaders_set = {groups[n][1] for n in names_input if n in groups}
            print(f"Множина ПІБ старост: {leaders_set}")

        elif choice == '10':
            print("Вихід з програми")
            break
        else:
            print("Невірний вибір, спробуйте ще раз.")

if __name__ == "__main__":
    main()