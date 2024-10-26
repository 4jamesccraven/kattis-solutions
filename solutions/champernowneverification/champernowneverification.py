def main() -> None:
    word = input()

    match word:
        case '1':
            print(1)
        case '12':
            print(2)
        case '123':
            print(3)
        case '1234':
            print(4)
        case '12345':
            print(5)
        case '123456':
            print(6)
        case '1234567':
            print(7)
        case '12345678':
            print(8)
        case '123456789':
            print(9)
        case _:
            print(-1)


if __name__ == '__main__':
    main()
