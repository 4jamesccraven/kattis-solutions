locs = {
    'a': (0, 0),
    'b': (0, 1),
    'c': (0, 2),
    'd': (0, 3),
    'e': (1, 0),
    'f': (1, 1),
    'g': (1, 2),
    'h': (1, 3),
    'i': (2, 0),
    'j': (2, 1),
    'k': (2, 2),
    'l': (2, 3),
    'm': (3, 0),
    'n': (3, 1),
    'o': (3, 2)
}


def main():
    board = []
    for _ in range(4):
        board.append(input().lower())

    board = [[i for i in line] for line in board]

    distance = {}

    for j, val in enumerate(board):
        for i, char in enumerate(val):
            if char == '.':
                continue
            distance[char] = (j, i)

    final_vals = []

    for char in locs.keys():
        wx, wy = distance[char]
        rx, ry = locs[char]

        val1 = abs(wx - rx)
        val2 = abs(wy - ry)

        final_vals.append(val1)
        final_vals.append(val2)

    print(sum(final_vals))


if __name__ == '__main__':
    main()
