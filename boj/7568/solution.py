# Migrated from ./boj/boj7568.py by boj_validator
from sys import stdin
from typing import Final

PersonSize = tuple[int, int]        # (키, 몸무게) 쌍의 튜플 타입
N: Final[int] = int(stdin.readline())
people: list[PersonSize] = [tuple(map(int, stdin.readline().split())) for _ in range(N)]

for person in people:
    rank: int = 1
    for other in people:
        if person[0] < other[0] and person[1] < other[1]:
            rank += 1
    print(rank)
