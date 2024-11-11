from collections import defaultdict, Counter
from functools import reduce
from itertools import chain
from operator import and_


def main() -> None:
    users = defaultdict(list)

    for _ in range(int(input())):
        name, *words = input().split()

        users[name].extend(words)

    vals = list(chain.from_iterable(users.values()))
    all_ = reduce(and_, map(set, users.values()))
    counts = Counter([val for val in vals if val in all_])

    if len(counts) == 0:
        print('all clear'.upper())
    else:
        curr_elems = []
        for word in counts.most_common():
            if len(curr_elems) == 0 or word[1] != curr_elems[-1][1]:
                for w in sorted(curr_elems):
                    print(w[0])
                curr_elems = []
                curr_elems.append(word)
            else:
                curr_elems.append(word)
        for w in sorted(curr_elems):
            print(w[0])


if __name__ == '__main__':
    main()
