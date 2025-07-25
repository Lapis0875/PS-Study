# Migrated from ./boj/boj27433.py by boj_validator
from sys import stdin, setrecursionlimit

setrecursionlimit(10 ** 6)

def factorial(x: int) -> int:
    return x * factorial(x - 1) if x > 1 else 1

print(factorial(int(stdin.readline())))
