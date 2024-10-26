def main() -> None:
    v: int = int(input())
    d: list[str] = input().split()

    digits: dict[str, int] = {k: v for k, v in zip(d, range(v))}
    decode: str = input()

    tokens = []
    while decode:
        token = tuple(key for key in digits.keys()
                      if decode.startswith(key))[0]
        tokens.append(token)

        index = len(token)
        decode = decode[index:]

    val = 0
    for place, token in enumerate(reversed(tokens)):
        m = v ** place
        val += digits[token] * (m if m > 0 else 1)

    print(val)


if __name__ == '__main__':
    main()
