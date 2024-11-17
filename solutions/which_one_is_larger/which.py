def main():
    a_raw = input()
    b_raw = input()

    a, b = map(float, [a_raw, b_raw])

    atp = tuple(map(int, a_raw.split('.')))
    btp = tuple(map(int, b_raw.split('.')))

    conditions = [
        a > b and atp > btp,
        b > a and btp > atp
    ]

    print(max(a,b) if any(conditions) else -1)


if __name__ == '__main__':
    main()
