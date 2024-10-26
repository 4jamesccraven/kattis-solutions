from math import sin, cos
from functools import partial


def price_long(p, a, b, c, d, k) -> float:
    return p * (sin(a * k + b) + cos(c * k + d) + 2)


def main() -> None:
    p, a, b, c, d, n = map(int, input().split())

    if n == 1:
        print(f'{0:.2f}')
        return

    price = partial(price_long, p=p, a=a, b=b, c=c, d=d)

    highest = price(k=1)

    vals = []
    for i in range(2, n + 1):
        p_i = price(k=i)
        if highest >= p_i:
            vals.append(highest - p_i)
        else:
            highest = p_i

    if len(vals) == 0:
        print(f'{0:.2f}')
        return

    print(max(vals))


if __name__ == '__main__':
    main()
