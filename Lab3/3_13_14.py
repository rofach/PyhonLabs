def encode_rle(text):
    if not text:
        return ""

    encoded_text = ""
    current_char = text[0]
    count = 1

    for index in range(1, len(text)):
        if text[index] == current_char:
            count += 1
        else:
            encoded_text += f"{current_char}{count}"
            current_char = text[index]
            count = 1

    encoded_text += f"{current_char}{count}"
    return encoded_text


def decode_rle(text):
    decoded_text = ""
    index = 0

    while index < len(text):
        char = text[index]
        index += 1
        number_text = ""

        while index < len(text) and text[index].isdigit():
            number_text += text[index]
            index += 1

        if number_text:
            decoded_text += char * int(number_text)

    return decoded_text


def main():
    text = input("Введіть рядок: ")
    encoded_text = encode_rle(text)
    print("Стиск:", encoded_text)
    print("Назад:", decode_rle(encoded_text))


if __name__ == "__main__":
    main()
