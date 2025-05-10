# Migrated from ./boj/boj2775.py by boj_validator
from sys import stdin
from typing import Final

T: Final[int] = int(stdin.readline())

# 0층 b호 -> b명
# 1층 b호 -> sum(1...b)
# 2층 b호 -> sum(sum(1)...sum(1...b))
# ...

residents: list[list[int]] = [[0 for _ in range(15)] for _ in range(15)]        # 0~14층, 1~14호 (0호실은 사용하지 않는다!)
for i in range(1, 15):      # 0층 채우기
    residents[0][i] = i

def get_resident(K: int, N: int) -> int:
    if residents[K][N] == 0:    # 아직 계산되지 않은 층 수
        total: int = 0
        for i in range(1, N + 1):
            total += get_resident(K - 1, i)
        residents[K][N] = total
    return residents[K][N]


for _ in range(T):
    K: Final[int] = int(stdin.readline())       # 층
    N: Final[int] = int(stdin.readline())       # 호
    print(get_resident(K, N))
