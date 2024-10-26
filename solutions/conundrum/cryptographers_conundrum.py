def main() -> None:
    orig = input().strip()

    times = len(orig) // 3

    goal = 'PER' * times

    print(len([a for a, b in zip(orig, goal) if a != b]))

if __name__ == '__main__':
    main()
