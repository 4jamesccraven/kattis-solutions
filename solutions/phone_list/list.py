def main() -> None:
    for _ in range(int(input())):
        len_nums = int(input())

        nums = [input() for _ in range(len_nums)]
        nums.sort()

        valid = True
        for i in range(1, len_nums):
            prev = nums[i - 1]
            curr = nums[i][:len(prev)]
            if curr == prev:
                valid = False
                break

        print('YES' if valid else 'NO')

if __name__ == '__main__':
    main()
