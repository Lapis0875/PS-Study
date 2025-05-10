# Migrated from ./boj/boj1312.py by boj_validator
from sys import stdin

A, B, N = map(int, stdin.readline().split())


"""
25 / 7 = 3 ... 4
40 / 7 = 5 ... 5
50 / 7 = 7 ... 1
...
"""
Q: int = A // B     # 소수점 위의 몫.
a: int = A % B      # 소수점 뒤의 숫자를 계산하기 위한 변수.
pos: int = 0        # 현재 자리수

while pos <= N:
    Q: int = a // B
    R: int = a % B
    a = R * 10
    pos += 1

print(Q)