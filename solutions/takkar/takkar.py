def main() -> None:
    a, b = int(input()), int(input())

    out = ''
    match (n := a - b):
        case n if n < 0:
            out = 'FAKE NEWS!'
        case n if n > 0:
            out = 'MAGA!'
        case 0:
            out = 'WORLD WAR 3!'

    print(out)


if __name__ == '__main__':
    main()
