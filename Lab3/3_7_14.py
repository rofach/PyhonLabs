import re


def check_identifier(word):
    return bool(re.fullmatch(r"[A-Za-z_][A-Za-z0-9_]*", word))


def main():
    word = input("Введіть слово: ")
    if check_identifier(word):
        print("Так")
    else:
        print("Ні")


if __name__ == "__main__":
    main()
