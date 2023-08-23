from sys import stdin
from typing import Final

MAX: Final[int] = 246913

sieve: list[int] = [False, False]
sieve.extend(True for _ in range(2, MAX))    # 123,456 * 2 - 1회 더 반복해 배열 미리 만들어두기.

for i in range(2, MAX):                      # 위에서 일부러 2 ~ 246913을 반복한 이유는, 파이썬의 int형 캐싱 방식 때문.
    if sieve[i]:
        j: int = 2
        while (x := i * j) <= MAX:
            sieve[x] = False
            j += 1

while True: 
    N: int = int(stdin.readline())
    if N == 0:
        break
    count: int = 0
    for i in range(N + 1, 2 * N + 1):
        if sieve[i]:
            count += 1
    print(count)
