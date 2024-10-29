# NOT A SOLUTION. It unfortunately times out ~half way through the test cases

from collections.abc import Callable
from functools import cache

SENTINEL = 1_000_000_000_000_000

def min_moves(grid: list[list[int]]) -> Callable:
    LR = len(grid)
    LC = len(grid[0])

    def valid_pair(row, col) -> bool:
        conditions = (0 <= row < LR, 0 <= col < LC)
        return all(conditions)

    @cache
    def min_moves_internal(
        row: int = 0,
        col: int = 0,
        curr_moves: int = 0,
        exclude: tuple[tuple[int, int]] = () # type: ignore
    ) -> int:
        # print(f'({row}, {col})')
        if (row, col) == (LR - 1, LC - 1):
            return curr_moves

        exclude = exclude + ((row, col),) # type: ignore
        # print(exclude)

        move_length = grid[row][col]

        if move_length == 0:
            return SENTINEL

        new_moves: list[tuple[int, ...]] = [
            (row + move_length, col),
            (row - move_length, col),
            (row, col + move_length),
            (row, col - move_length),
        ]

        new_moves = [val for val in new_moves
                     if valid_pair(*val) and val not in exclude]

        if len(new_moves) == 0:
            return SENTINEL

        to_minimise = [min_moves_internal(*move, curr_moves + 1, exclude) for move in new_moves]
        # print(to_minimise)
        return min(to_minimise)

    return min_moves_internal


def main() -> None:
    n, _ = map(int, input().split())

    grid: list[list[int]] = [[int(val) for val in row]
                             for row in [input() for _ in range(n)]]

    print(val if (val := min_moves(grid)()) != SENTINEL else -1)

if __name__ == '__main__':
    main()
