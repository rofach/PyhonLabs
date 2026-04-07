def show_p_letters(amount):
    if not 1 <= amount <= 9:
        print("Помилка")
        return

    rows = [""] * 6
    for number in range(1, amount + 1):
        rows[0] += " ____  "
        rows[1] += "|    \\ "
        rows[2] += f"| {number}  | "
        rows[3] += "|____/ "
        rows[4] += "|      "
        rows[5] += "|      "

    for row in rows:
        print(row.rstrip())


def main():
    amount = int(input("Введіть число: "))
    show_p_letters(amount)


if __name__ == "__main__":
    main()
