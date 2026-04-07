def reverse_each_word(sentence):
    words = sentence.split()
    changed_words = [word[::-1] for word in words]
    return " ".join(changed_words)


def main():
    sentence = input("Введіть речення: ")
    print("Результат:", reverse_each_word(sentence))


if __name__ == "__main__":
    main()
