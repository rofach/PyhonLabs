import re


def collect_unique_words(sentence):
    words = re.findall(r"[A-Za-zА-Яа-яІіЇїЄєҐґ]+", sentence)
    unique_list = []
    for word in words:
        if word not in unique_list:
            unique_list.append(word)
    return unique_list


def main():
    sentence = input("Введіть речення: ")
    unique_words = collect_unique_words(sentence)
    print(" ".join(unique_words))


if __name__ == "__main__":
    main()
