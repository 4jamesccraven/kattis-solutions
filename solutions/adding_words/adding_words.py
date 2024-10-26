def main() -> None:
    stack: list[list[str]] = []
    while True:
        try:
            stack.append(input().split())
        except EOFError:
            break

    definitions: dict[str, int] = {}

    for command, *args in stack:
        match command:
            case 'def':
                definitions[args[0]] = int(args[1])
            case 'clear':
                definitions.clear()
            case 'calc':
                to_print = ' '.join(args)

                if any(definitions.get(val) is None
                       for val in args[::2]):
                    print(f'{to_print} unknown')
                    continue

                vals = [definitions.get(val)
                        if args[(i * 2) - 1] != '-'
                        else definitions.get(val) * -1
                        for i, val in enumerate(args[::2])]

                result = sum(vals)
                result = next(filter(lambda x: definitions[x] == result,
                              definitions), 'unknown')

                print(f'{to_print} {result}')


if __name__ == '__main__':
    main()
