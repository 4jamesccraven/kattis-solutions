from itertools import pairwise, starmap
from operator import sub
from sys import stdin


def main() -> None:
    groups = [line.split() for line in stdin]

    for line in groups:
        n, *nums = map(int, line)

        if len(nums) == 1:
            print('Jolly')
            continue

        differences = tuple(abs(val) for val in starmap(sub, pairwise(nums)))

        differences = tuple(reversed(sorted(differences)))

        ideal = tuple(reversed(range(n)))[:-1]

        print('Jolly' if differences == ideal else 'Not jolly')

if __name__ == '__main__':
    main()
