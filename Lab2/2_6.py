def main():
    try:
        line = input().strip()
        if not line:
            return
        n = int(line)
    except ValueError:
        return

    possible_numbers = set(range(1, n + 1))

    while True:
        line = input().strip()
        
        if line == "Все":
            break
        
        try:
            question_set = set(map(int, line.split()))
        except ValueError:
            continue

        yes_variants = possible_numbers.intersection(question_set)
        
        no_variants = possible_numbers.difference(question_set)

        if len(yes_variants) > len(no_variants):
            print("Так")
            possible_numbers = yes_variants
        else:
            print("Hi")
            possible_numbers = no_variants

    result = sorted(list(possible_numbers))
    print(*(result))

if __name__ == "__main__":
    main()