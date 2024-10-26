def main() -> None:
    for _ in range(int(input())):
        inp = input()
        nums: list[int] = [int(x) if x else 0 for x in inp.split(',')]

        powers = len(nums)

        print(sum(val * (60**power) for val, power in zip(nums, reversed(range(powers)))))

if __name__ == '__main__':
    main()

