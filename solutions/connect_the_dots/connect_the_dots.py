from itertools import groupby
from string import ascii_letters, digits
from sys import stdin
import re

DOTS = list(digits)
DOTS.extend(ascii_letters)


def connect_the_dots(game: list[str]) -> None:
    def t(g: list[str]) -> list[str]:
        '''Transpose the game to avoid rewriting logic'''
        return [''.join(line) for line in zip(*g)]

    def assign(col_no, text) -> None:
        t_game[col_no] = text
        for i, char in enumerate(text):
            game[i] = game[i][:col_no] + char + game[i][col_no + 1:]

    t_game = t(game)

    r = True
    row, column = 0, 0
    for i, line in enumerate(game):
        if (c := line.find('0')) != -1:
            row, column = i, c
    else:
        r = False

    if r:
        return

    dot = 1
    while True:
        if dot > len(DOTS) - 1:
            break
        if (dot_pos := game[row].find(DOTS[dot])) != -1 and dot_pos > column:
            between = game[row][column + 1:dot_pos]
            between = re.sub(r'\|', '+', between)
            between = re.sub(r'\.', '-', between)

            game[row] = game[row][:column + 1] + between + game[row][dot_pos:]

            column = dot_pos
            dot += 1
            t_game = t(game)
        elif dot_pos != -1 and dot_pos < column:
            between = game[row][dot_pos + 1:column] 
            between = re.sub(r'\|', '+', between)
            between = re.sub(r'\.', '-', between)

            game[row] = game[row][:dot_pos + 1] + between + game[row][column:]

            column = dot_pos
            dot += 1
            t_game = t(game)
        elif (dot_pos := t_game[column].find(DOTS[dot])) != -1 and dot_pos > row:
            between = t_game[column][row + 1:dot_pos]
            between = re.sub(r'\-', '+', between)
            between = re.sub(r'\.', '|', between)

            new_col = t_game[column][:row + 1] + between + t_game[column][dot_pos:]
            assign(column, new_col)

            row = dot_pos
            dot += 1
        elif dot_pos != -1 and dot_pos < row:
            between = t_game[column][dot_pos + 1:row]
            between = re.sub(r'\-', '+', between)
            between = re.sub(r'\.', '|', between)

            new_col = t_game[column][:dot_pos + 1] + between + t_game[column][row:]
            assign(column, new_col)

            row = dot_pos
            dot += 1
        else:
            break


def main() -> None:
    games = [line.strip() for line in stdin]

    games = [list(group) for k, group in groupby(games, lambda x: x != '') if k]

    for game in games:
        connect_the_dots(game)
        for line in game:
            print(line)
        print()

if __name__ == '__main__':
    main()
