# Migrated from ./boj/boj2108.py by boj_validator
from collections import Counter
from sys import stdin
from typing import Final

N: Final[int] = int(stdin.readline())
numbers: list[int] = sorted(int(stdin.readline()) for _ in range(N))


if N > 1:
    print(round(sum(numbers) / N))
    print(numbers[N // 2])

    counted: list[tuple[int, int]] = Counter(numbers).most_common()
    maxCount: int = counted[0][1]
    most_commons: list[int] = [counted[0][0]]
    for i, c in counted[1:]:
        if c < maxCount:
            break
        most_commons.append(i)

    print(most_commons[1] if len(most_commons) > 1 else most_commons[0])
    print(numbers[-1] - numbers[0])
else:
    n: int = numbers[0]
    print(n)
    print(n)
    print(n)
    print(0)