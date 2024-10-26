def main() -> None:
    e, f, c, *_ = tuple(map(int, input().split()))

    count = e + f
    price = c

    drunk = 0

    while count >= price:
        cbp: int = count // price

        count = count % price
        count += cbp
        drunk += cbp

    print(drunk)


if __name__ == '__main__':
    main()
