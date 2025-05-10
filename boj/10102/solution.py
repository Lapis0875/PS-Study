# Migrated from ./boj/boj10102.py by boj_validator
from sys import stdin
from typing import Final

V: Final[int] = int(stdin.readline())
cntA: int = 0
cntB: int = 0
for vote in stdin.readline()[:-1]:
    if vote == "A":
        cntA += 1
    else:
        cntB += 1

if cntA > cntB:
    print("A")
elif cntA < cntB:
    print("B")
else:
    print("Tie")
