from math import sqrt


def main() -> None:
    for _ in range(int(input())):
        a, b, c = map(int, input().split())

        radicand = (b * b) - (4 * a * c)

        if radicand >= 0:
            radicand = sqrt(radicand)
        else:
            print('NO')
            continue

        print('YES' if radicand == int(radicand) else 'NO')


if __name__ == '__main__':
    main()
