def find_top_symbols(text, allowed_symbols):
    symbol_counts = {}
    for symbol in text:
        if symbol in allowed_symbols:
            symbol_counts[symbol] = symbol_counts.get(symbol, 0) + 1

    if not symbol_counts:
        return []

    top_count = max(symbol_counts.values())
    return [symbol for symbol, amount in symbol_counts.items() if amount == top_count]


def main():
    text = input("Введіть рядок: ")
    allowed_symbols = set(input("Введіть символи: "))
    top_symbols = find_top_symbols(text, allowed_symbols)
    if top_symbols:
        print("Часті:", " ".join(top_symbols))
    else:
        print("Нема")


if __name__ == "__main__":
    main()
