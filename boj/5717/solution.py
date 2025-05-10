# Migrated from ./boj/boj5717.py by boj_validator
from sys import stdin

while (i := stdin.readline()) != "0 0\n":
    print(eval(i.replace(*" +")))