# NOT A SOLUTION. Wrong answer on test case 81

from collections.abc import Callable
from math import inf
from typing import Union

SENTINEL = inf

def min_moves(grid: list[list[int]]) -> Callable:
    LR = len(grid)
    LC = len(grid[0])
    CACHE: dict[tuple, Union[int, float]] = {}

    def valid_pair(row, col) -> bool:
        conditions = (0 <= row < LR, 0 <= col < LC)
        return all(conditions)

    def min_moves_internal(
        row: int = 0,
        col: int = 0,
        exclude: tuple[tuple[int, int]] = () # type: ignore
    ) -> Union[int, float]:
        if (k := (row, col)) in CACHE:
            return CACHE[k]

        if (row, col) == (LR - 1, LC - 1):
            return 0

        exclude = exclude + ((row, col),) # type: ignore

        move_length = grid[row][col]

        if move_length == 0:
            CACHE[(row, col)] = SENTINEL
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
            CACHE[(row, col)] = SENTINEL
            return SENTINEL

        to_minimise = [min_moves_internal(*move, exclude) # type: ignore
                       for move in new_moves]
        r_val = 1 + min(to_minimise)

        CACHE[(row, col)] = r_val

        return r_val

    return min_moves_internal


def main() -> None:
    n, _ = map(int, input().split())

    grid: list[list[int]] = [[int(val) for val in row]
                             for row in [input() for _ in range(n)]]

    print(val if (val := min_moves(grid)()) < SENTINEL else -1)

if __name__ == '__main__':
    main()
