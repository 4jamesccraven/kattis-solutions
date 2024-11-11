from itertools import chain, starmap
from operator import mul


def dot(x, y) -> int:
    return sum(starmap(mul, zip(x, y)))


def main():
    m_h, m_w, k_h, k_w = map(int, input().split())

    M = [list(map(int, input().split())) for _ in range(m_h)]

    K = [val[::-1] for val in [list(map(int, input().split())) for _ in range(k_h)][::-1]]

    Kv = list(chain.from_iterable(K))

    for i in range(m_h - k_h + 1):
        line = []
        for j in range(m_w - k_w + 1):
            Mv = [val[j:j + k_w] for val in M[i:i + k_h]]
            Mv = list(chain.from_iterable(Mv))
            line.append(dot(Mv, Kv))
        print(*line, sep=' ')


if __name__ == '__main__':
    main()