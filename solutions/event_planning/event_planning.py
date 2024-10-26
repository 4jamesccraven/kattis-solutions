def main() -> None:
    participants, budget, hotels, _ = map(int, input().split())

    possible_prices: list[int] = []
    for _ in range(hotels):
        price = int(input()) * participants

        if any(beds >= participants
               for beds in map(int, input().split())):
            possible_prices.append(price)

    try:
        p = min(price for price in possible_prices)
    except ValueError:
        print('stay home')
        return

    print(p if p <= budget else 'stay home')


if __name__ == '__main__':
    main()
