# Migrated from ./boj/boj9020.py by boj_validator
from sys import stdin
from typing import Final

T: Final[int] = int(stdin.readline())

sieve: list[int] = [False, False]
lastSieved: int = 1

def greedyEratos(max: int):
    global lastSieved
    sieve.extend(True for _ in range(N - lastSieved + 1))

    for i in range(2, N + 1):
        if sieve[i]:
            j: int = 2
            while (x := i * j) <= N:
                sieve[x] = False
                j += 1
    lastSieved = N

for _ in range(T):
    N: Final[int] = int(stdin.readline())
    
    if N >= lastSieved:         # 새로 필요해진 부분에 대해 에라토스테네스의 체를 마저 진행한다.
        greedyEratos(N)
    
    for i in range(N // 2, 1, -1):
        if sieve[i] and sieve[N - i]:
            print(i, N - i)
            break
