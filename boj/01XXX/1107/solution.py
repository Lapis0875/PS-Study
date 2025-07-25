# Migrated from ./boj/boj1107.py by boj_validator
from sys import stdin
from typing import Final

N: Final[int] = int(stdin.readline())
M: Final[int] = int(stdin.readline())
broken: list[int] = list(map(int, stdin.readline().split()))
usable: list[int] = []
for i in range(10):
    if i not in broken:
        usable.append(i)

# 0. N의 자리수 세기
digits: int = 0
n: int = N
while n > 0:
    digits += 1
    n //= 10

moving: int = 100                   # 초기 번호는 100번이다.
count: int = 0                      # 버튼을 누른 횟수

if digits == 3:
    if N < M:
        while N == M:
            N += 1
            count += 1
    else:
        while N == M:
            N -= 1
            count += 1
else:
    for i in range(digits):
        for number in usable:
            cur_count: int = 0

print(count)