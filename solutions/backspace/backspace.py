def main() -> None:
    inp = input()

    final = []

    for char in inp:
        if char != '<':
            final.append(char)
        else:
            final.pop()

    print(''.join(final))


if __name__ == '__main__':
    main()
