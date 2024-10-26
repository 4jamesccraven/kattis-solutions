import math


def main() -> None:
    h, v = map(int, input().split())

    if 0 <= v <= 180:
        print('safe')
    else:
        print(int(h // math.sin(math.radians(v - 180))))

if __name__ == '__main__':
    main()
