from sys import stdin
from typing import Final


T: Final[int] = int(stdin.readline())
for _ in range(T):
    cnt: Final[int] = int(stdin.readline())
    yangjojang: str = ""
    L: int = 0
    for _ in range(cnt):
        school, lstr = stdin.readline().split()
        if (l := int(lstr)) > L:
            yangjojang = school
            L = l
    print(yangjojang)