def hide_card_number(card_number):
    digits_only = card_number.replace(" ", "")
    if len(digits_only) != 16 or not digits_only.isdigit():
        return "Помилка"
    return f"**** **** **** {digits_only[-4:]}"


def main():
    card_number = input("Введіть номер: ")
    print("Маска:", hide_card_number(card_number))


if __name__ == "__main__":
    main()
