from itertools import combinations


def score(scores: list[int]) -> float:
    return (1/5) * sum(s * (4**i / 5**i) for i, s in enumerate(scores))


def main() -> None:
    scores = [int(input()) for _ in range(int(input()))]

    print (score(scores))

    vals = [score(list(comb)) for comb in combinations(scores, len(scores) - 1)]

    print(sum(vals) / len(vals))


if __name__ == '__main__':
    main()
