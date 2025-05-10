# Migrated from ./boj/boj1316.py by boj_validator
from sys import stdin

N: int = int(stdin.readline())

cnt: int = 0
for _ in range(N):
    word: str = stdin.readline()[:-1]
    check: dict[str, bool] = {chr(ord("a") + i): False for i in range(26)}
    before: str = ""
    for c in word:
        if before != c:
            if not check[c]:
                check[c] = True
                before = c
            else:
                break
    else:
        cnt += 1

print(cnt)
