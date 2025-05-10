# Migrated from ./boj/boj10870.py by boj_validator
from sys import stdin

memo: list[int] = [0, 1]
memo_len: int = 2

def fibonacci(x: int) -> int:
    global memo_len
    if memo_len <= x:
        for i in range(memo_len, x + 1):
            memo.append(memo[i - 1] + memo[i - 2])
        memo_len = len(memo)
    return memo[x]

print(fibonacci(int(stdin.readline())))
