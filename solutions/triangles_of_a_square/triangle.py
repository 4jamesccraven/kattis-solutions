# James coding, Matt Solution


from enum import Enum

class Coord(Enum):
    corner = -1
    side = 0


def gen_coord(a, b):
    if all((a == 0 or a == 2024,
            b == 0 or b == 2024)):
        return Coord.corner
    else:
        return Coord.side


def main():
    a, b, c, d = map(int, input().split())

    beg = gen_coord(a, b)
    end = gen_coord(c, d)

    count = -1
    match (beg, end):
        case [Coord.corner, Coord.side]:
            count = 1
        case [Coord.side, Coord.corner]:
            count = 1
        case [Coord.side, Coord.side]:
            count = 2
        case [Coord.corner, Coord.corner]:
            count = 0
        
    print(count)

if __name__ == '__main__':
    main()
