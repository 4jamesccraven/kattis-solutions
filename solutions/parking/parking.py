

def main() -> None:
    cases: int = int(input())

    for _ in range(cases):
        total: int = int(input())
        vals = list(map(int, input().split()))

        mid_point: int = round(sum(vals) / total)

        low: int = min(vals)
        high: int = max(vals)

        print(2 * (mid_point - low) + 2 * (high - mid_point))


if __name__ == '__main__':
    main()
