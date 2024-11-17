def main():
    rows, length = map(int, input().split())

    lg = False
    for word in [input() for _ in range(rows)]:
        diff = length - len(word)

        if diff == 0:
            print(word)
        else:
            half = diff // 2
            l, r = (diff - half, half) if lg else (half, diff - half)

            if l != r:
                print(('.' * l) + word + ('.' * r))
                lg = not lg
            else:
                print(f'{word:.^{length}}')


if __name__ == '__main__':
    main()
