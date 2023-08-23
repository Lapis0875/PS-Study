from collections import Counter
from sys import stdin
from typing import Final


N: Final[int] = int(stdin.readline())
prizes: list[int] = []
for _ in range(N):
    eyes: tuple[int, int, int] = tuple(map(int, stdin.readline().split()))
    count: list[tuple[int, int]] = Counter(eyes).most_common()
    
    if count[0][1] == 3:
        prizes.append(10000 + count[0][0] * 1000)
    elif count[0][1] == 2:
        prizes.append(1000 + count[0][0] * 100)
    else:
        prizes.append(max(eyes) * 100)

print(max(prizes))