from collections import Counter


def main() -> None:
    num_cases = int(input())
    cases = [input() for _ in range(2 * num_cases)]
    cases = cases[1::2]

    for case in cases:
        g_counts = dict(Counter(case))
        g_wait = {k: (case.rindex(k) + 1) * 5 for k in set(case)}
        case = ''.join(sorted(case, key=lambda x: g_wait[x]))
        g_new_wait = {k: (case.rindex(k) + 1) * 5 for k in set(case)}

        wait = sum(g_counts[k] * g_wait[k] for k in g_wait.keys())
        new_wait = sum(g_counts[k] * g_new_wait[k] for k in g_wait.keys())
        print(wait - new_wait)


if __name__ == '__main__':
    main()
