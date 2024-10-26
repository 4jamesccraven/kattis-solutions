def main() -> None:
    rows, _ = map(int, input().split())

    all_words: list[str] = []

    row_vals = [input() for _ in range(rows)]
    all_words.extend([word for line in row_vals
                      for word in line.split('#')
                      if len(word) >= 2])

    row_vals = [''.join(line) for line in
                zip(*[list(word) for word in row_vals])]
    all_words.extend([word for line in row_vals
                      for word in line.split('#')
                      if len(word) >= 2])

    print(min(all_words))


if __name__ == '__main__':
    main()
