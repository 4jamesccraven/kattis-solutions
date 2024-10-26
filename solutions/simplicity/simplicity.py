from collections import Counter


def main() -> None:
    dist = dict(Counter(input()))

    if len(dist) <= 2:
        print(0)
    else:
        removed = 0
        while len(dist) > 2:
            next_to_remove = min(dist.keys(), key=lambda x: dist[x])
            removed += dist.pop(next_to_remove)

        print(removed)


if __name__ == '__main__':
    main()
