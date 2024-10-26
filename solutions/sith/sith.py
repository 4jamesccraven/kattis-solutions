def main() -> None:
    input()
    a, b, ab = map(int, (input() for _ in range(3)))

    if a >= b:
        print('VEIT EKKI')
    else:
        print('JEDI' if ab < 0 else 'SITH')


if __name__ == '__main__':
    main()
