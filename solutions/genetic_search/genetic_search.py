import re


def main() -> None:
    inp = input()

    while inp != '0':
        s, l = inp.split()

        type_1 = sum(1 for _ in re.finditer(f'(?={s})', l))

        drop_one = set(s[:i] + s[i + 1:] for i in range(len(s)))
        type_2 = sum(sum(1 for _ in re.finditer(f'(?={t})', l))
                     for t in drop_one)

        CHARS = ('A', 'C', 'G', 'T')
        add_one = set(s[:i] + char + s[i:] for char in CHARS
                      for i in range(len(s) + 1))
        type_3 = sum(sum(1 for _ in re.finditer(f'(?={t})', l))
                     for t in add_one)

        print(f'{type_1} {type_2} {type_3}')
        inp = input()


if __name__ == '__main__':
    main()
