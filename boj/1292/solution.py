# Migrated from ./boj/boj1292.py by boj_validator
from sys import stdin

A, B = map(int, stdin.readline().split())

cnt: int = 0        # 각 항의 개수 (1, 2, 2, 3, 3, 3, ...)
sum: int = 0        # 구간 합
i: int = 1          # 수열의 현재 항
n: int = 1          # 수열의 현재 항 번호

while n <= B:
    cnt += 1
    if n >= A:
        sum += i
    
    if cnt == i:
        cnt = 0
        i += 1
    n += 1

print(sum)
