# Migrated from ./boj/boj5086.py by boj_validator
from sys import stdin

while (i := stdin.readline()) != "0 0\n":
    x, y = map(int, i.split())
    if y % x == 0:
        print("factor")
    elif x % y == 0:
        print("multiple")
    else:
        print("neither")