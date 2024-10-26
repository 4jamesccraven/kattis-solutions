from functools import cache


@cache
def find_min_remaining(row: str) -> int:
    child_vals: list[int] = []

    for i in range(21):
        if row[i:i + 3] == 'oo-':
            child_vals.append(find_min_remaining(row[:i] + '--o' + row[i+3:]))

    row_reversed = row[::-1]
    for i in range(21):
        if row_reversed[i:i + 3] == 'oo-':
            child_vals.append(find_min_remaining(row_reversed[:i] + '--o' + row_reversed[i+3:]))

    if len(child_vals) == 0:
        return row.count('o')
    else:
        return min(child_vals)


def main() -> None:
    for _ in range(int(input())):
        print(find_min_remaining(input()))


if __name__ == '__main__':
    main()
