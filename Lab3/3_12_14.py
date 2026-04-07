import re


def replace_forbidden_words(text, banned_words):
    clean_text = text
    for word in banned_words:
        pattern = r"\b" + word + r"\b"
        clean_text = re.sub(pattern, "[ЦЕНЗУРА]", clean_text, flags=re.IGNORECASE)
    return clean_text


def main():
    text = input("Введіть текст: ")
    banned_words = [word.strip() for word in input("Введіть слова: ").split(",")]
    print("Результат:", replace_forbidden_words(text, banned_words))


if __name__ == "__main__":
    main()
