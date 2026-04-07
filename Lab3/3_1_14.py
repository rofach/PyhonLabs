def get_digit_count(text):
    digit_count = 0
    for symbol in text:
        if symbol.isdigit():
            digit_count += 1
    return digit_count


def main():
    text = input("Введіть рядок: ")
    digit_count = get_digit_count(text)
    print("Цифри:", digit_count)


if __name__ == "__main__":
    main()
