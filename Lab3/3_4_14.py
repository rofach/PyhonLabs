def check_palindrome(word):
    lowered_word = word.lower()
    word_length = len(lowered_word)
    for index in range(word_length // 2):
        if lowered_word[index] != lowered_word[word_length - 1 - index]:
            return False
    return True


def main():
    word = input("Введіть слово: ")
    if check_palindrome(word):
        print("Так")
    else:
        print("Ні")


if __name__ == "__main__":
    main()
