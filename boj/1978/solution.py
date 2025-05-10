# Migrated from ./boj/boj1978.py by boj_validator
from sys import stdin
from typing import Final

sieve: Final[list[bool]] = [False, False]      # 0, 1은 소수가 아니다.
sieve.extend(True for _ in range(999))  # 0~1000까지의 인덱스를 가지는 에라토스테네스의 체 배열

for i in range(2, 1001):
    if sieve[i]:
        j: int = 2
        while (x := i * j) <= 1000:
            sieve[x] = False
            j += 1
N: Final[int] = int(stdin.readline())

print(sum(map(lambda s: sieve[int(s)], stdin.readline().split())))
    