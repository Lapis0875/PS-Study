# Migrated from ./boj/boj11729.py by boj_validator
from sys import stdin

N: int = int(stdin.readline())

def hanoi(plate: int, start: int, via: int, to: int):
    hanoi(plate - 1, start, via, to)
    print(start, to)
