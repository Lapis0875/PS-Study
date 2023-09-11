from sys import stdin
from typing import Final

N: Final[int] = int(stdin.readline())

count: int = 0
i: int = 1
while i <= N // 3:
    remaining: int = N - i
    j: int = 1
    k: int = remaining - j
    while j < max(remaining, i):
        k = remaining - j
        if k < j:       # 반드시 K가 최대가 되게 만든다. j가 k보다 커지면 앞선 경우를 반복하기 때문이다.
            break
        if k < i + j and i <= j:
                count += 1
        j += 1
    i += 1

print(count)
