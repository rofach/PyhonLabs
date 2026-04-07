def get_special_symbol_positions(text):
    allowed_letters = set(
        "abcdefghijklmnopqrstuvwxyz"
        "абвгґдеєжзиіїйклмнопрстуфхцчшщьюя"
        "абвгдеёжзийклмнопрстуфхцчшщъыьэюя"
    )
    positions = []

    for index, symbol in enumerate(text, start=1):
        if symbol == " ":
            continue
        if symbol.lower() not in allowed_letters:
            positions.append(index)

    return positions


def main():
    text = input("Введіть рядок: ")
    positions = get_special_symbol_positions(text)
    print("Кількість:", len(positions))
    print("Позиції:", " ".join(map(str, positions)))


if __name__ == "__main__":
    main()
