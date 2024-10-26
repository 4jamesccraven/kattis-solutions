# NOT A SOLUTION

from typing import Optional


DATES = [31, 28, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31] # type: ignore
DATES: dict[int, int] = {i: v for i, v in zip(range(1, 13), DATES)}


def find_valid(
        month: int,
        a: int, 
        b: int
) -> Optional[list[tuple[int, ...]]]:
    days: int = DATES.get(month, -1)
    rlist: list[tuple[int, ...]] = []

    if days == -1:
        return None

    day, year = a, b
    year = year + 2000 if 0 <= year <= 999 else year
    leap_year: bool = (year % 4 == 0 and year % 100 != 0) \
            or all(year % val == 0 for val in [4, 100, 400])
    addby: int = 2 if leap_year and month == 2 else 1
    if day in range(1, days + addby) and 2000 <= year <= 2999:
        rlist.append((month, day, year))

    year, day = a, b
    year = year + 2000 if 0 <= year <= 999 else year
    leap_year = (year % 4 == 0 and year % 100 != 0) \
            or all(year % val == 0 for val in [4, 100, 400])
    addby = 2 if leap_year and month == 2 else 1
    if day in range(1, days + addby) and 2000 <= year <= 2999:
        rlist.append((month, day, year))

    return rlist


def main() -> None:
    dateline: str = input()
    numbers: list[int] = list(map(int, (i for i in dateline.split('/'))))

    possible_months: list[int] = [num for num in numbers if num in range(1, 13)]

    possible_dates = []
    possible_dates = [date for date in possible_dates if date is not None]
    for month in possible_months:
        if s := find_valid(month, *(set(numbers) - set([month]))):
            possible_dates.extend(s)

    if len(possible_dates) == 0:
        print(f'{dateline} is illegal')
    else:
        date = sorted(possible_dates)[0]
        month, day, year = date

        print(f'{year}-{str(month).zfill(2)}-{str(day).zfill(2)}')


if __name__ == '__main__':
    main()

