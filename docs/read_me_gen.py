import os
import re
import requests
from functools import partial
from collections.abc import Iterable

from tqdm import tqdm

tqdm = partial(tqdm,
               bar_format='{desc}: [{bar}] {percentage:3.0f}%',
               ncols=50,
               ascii='-=',)


def problem_url(problem: str) -> str:
    return f'https://open.kattis.com/problems/{problem}'


def url_exists(problem: str) -> bool:
    try:
        response = requests.head(url=problem, allow_redirects=True)

        return response.status_code < 400

    except Exception as e:
        print(e)
        return False


def max_length(values: Iterable[str]) -> int:
    return len(max(values, key=lambda x: len(x)))


def render(table: list[str]) -> str:
    return f'''Kattis Solutions
----------------

This repo contains all my solutions to kattis problems
from my time on WU's programming team, as well as some
I did for fun. Note that this code is not meant to be
the most well formatted; its purpose is to solve the
problem as quickly as possible.

Problems
--------

{'\n'.join(table)}'''


def images(directories: list[str]) -> list[str]:
    supported_langs = {
        'py': 'python.png',
        'cpp': 'cpp.png',
        'rs': 'rust.png',
    }

    col = ['' for _ in range(len(directories))]
    for i, dir in enumerate(directories):
        path = os.path.join('./solutions/', dir)

        for file in os.listdir(path):
            for lang, img in supported_langs.items():
                if re.fullmatch(f'.*\\.{lang}$', file):
                    col[i] = col[i] + f' [![{lang}](images/{img})]()'

    return col



def main() -> None:
    problem_names = [file for file in os.listdir('solutions')
                     if  file != 'competition-spring2024'
                     and file != 'icpc']
    problem_names.sort()

    problem_urls = [problem_url(file.replace('_', ''))
                    for file in problem_names]

    for problem in tqdm(problem_urls, desc='Checking urls'):
        if not url_exists(problem):
            print(f'WARNING: {problem} is not a valid url')

    print('Writing README.md')

    problem_urls = [f'[{name}]({url})' for name, url in zip(problem_names, problem_urls)]
    solutions = [f'[source 🔗](solutions/{dir})' for dir in problem_names]

    w1, w2 = map(max_length, [problem_urls, solutions])

    table: list[str] = [
        f'| {'Problem':^{w1}} | {'Solution':^{w2 + 1}} | Languages |',
        f'|{'-' * (w1 + 2)}|{'-' * (w2 + 3)}|{'-'*11}',
    ]


    imgs = images(problem_names)
    for url, sol, img in zip(problem_urls, solutions, imgs):
        table.append(f'| {url:<{w1}} | {sol:<{w2}} | {img} |')

    document = render(table=table)

    with open('README.md', 'w', encoding='utf8') as f:
        f.write(document)

if __name__ == '__main__':
    main()
