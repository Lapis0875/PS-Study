# Migrated from ./boj/boj4101.py by boj_validator
from sys import stdin


while True:
    line: str = stdin.readline()
    if line == "0 0":
        break
    
    A, B = map(int, line.split(" "))
    print("Yes" if A > B else "No")