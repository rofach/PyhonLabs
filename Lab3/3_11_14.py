def get_letter_percentages(text):
    vowels = "аеєиіїоуюяaeiouy"
    total_letters = 0
    vowel_count = 0

    for symbol in text.lower():
        if symbol.isalpha():
            total_letters += 1
            if symbol in vowels:
                vowel_count += 1

    if total_letters == 0:
        return 0, 0

    consonant_count = total_letters - vowel_count
    vowel_percent = vowel_count * 100 / total_letters
    consonant_percent = consonant_count * 100 / total_letters
    return vowel_percent, consonant_percent


def main():
    text = input("Введіть текст: ")
    vowel_percent, consonant_percent = get_letter_percentages(text)
    print("Голосні:", round(vowel_percent, 2), "%")
    print("Приголосні:", round(consonant_percent, 2), "%")


if __name__ == "__main__":
    main()
