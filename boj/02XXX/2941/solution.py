# Migrated from ./boj/boj2941.py by boj_validator
from sys import stdin

text: str = stdin.readline()[:-1]
# kroatia: list[str] = ["c=", "c-", "dz=", "d-", "lj", "nj", "s=", "z="]
# for k in kroatia:
#     text = text.replace(k, "1")
# print(len(text))
N: int = len(text)
i: int = 0
cnt: int = 0

while i < N - 1:
    c: str = text[i]
    c2: str = text[i + 1]
    match c2:
        case "-" if c == "c" or c == "d":                           # c- & d-
            i += 2
        case "j" if c == "l" or c == "n":                           # lj & nj
            i += 2
        case "=" if c == "s" or c == "z" or c == "c":               # c= & s= & z=
            i += 2
        case "z" if c == "d" and i < N - 2 and text[i+2] == "=":    # dz=
            i += 3
        case _:                                                     # ETC
            i += 1
    cnt += 1

if i == N - 1:
    cnt += 1

print(cnt)
