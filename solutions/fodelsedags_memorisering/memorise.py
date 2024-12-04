from itertools import groupby


def main() -> None:
    entries = []
    for _ in range(int(input())):
        name, rank, birthday = input().split()

        rank = int(rank)
        birthday = tuple(map(int, birthday.split('/')))[::-1]

        entries.append((name, birthday, rank))

    entries.sort(key=lambda x: x[1])

    friends = []
    for _, g in groupby(entries, lambda x: x[1]):
        friend = sorted(g, key=lambda x: x[2])[-1][0]
        friends.append(friend)

    print(len(friends))
    for name in sorted(friends):
        print(name)


if __name__ == '__main__':
    main()
