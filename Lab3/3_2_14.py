def get_substring_count(text, piece):
    match_count = 0
    if not piece:
        return 0

    piece_len = len(piece)
    for index in range(len(text) - piece_len + 1):
        if text[index:index + piece_len] == piece:
            match_count += 1
    return match_count


def main():
    text = input("Введіть рядок: ")
    piece = input("Введіть підрядок: ")
    match_count = get_substring_count(text, piece)
    print("Кількість:", match_count)


if __name__ == "__main__":
    main()
