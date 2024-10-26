def find_islands(nums: list[int]) -> int:
    cmp: list[int] = [nums[0]]
    islands: int = 0

    for idx, num in enumerate(nums[1:]):
        if num > cmp[-1]:
            for i in range(cmp[-1] + 1, num + 1):
                if i in nums[idx:] and i not in cmp:
                    cmp.append(i)
                    islands += 1
        else:
            while cmp and num < cmp[-1]:
                cmp.pop()

            if not cmp:
                cmp.append(num)

    return islands


def main() -> None:
    num_cases = int(input())

    cases: list[list[int]] = [list(map(int, input()[1:].split())) for _ in range(num_cases)] 

    for idx, case in enumerate(cases, start=1):
        print(f'{idx} {find_islands(case)}')

if __name__ == '__main__':
    main()
