from sys import stdin
from typing import Final, Literal, cast

type Zebra = list[Literal["0", "1"]]

N: Final[int]
L: Final[int]
N, L = map(int, stdin.readline().split())
counted: dict[int, int] = {}

def count(zebra: Zebra) -> int:
    is_black: bool = False
    cnt: int = 0
    for color in zebra:
        match color:
            case "0":
                if is_black:
                    cnt += 1
                is_black = False
            case "1":
                is_black = True
    if is_black:    # 1로 끝나는 경우 처리
        cnt += 1
    return cnt

maxcnt: int = 0
for _ in range(N):
    zebra = cast(Zebra, stdin.readline()[:-1])
    cnt = count(zebra)
    maxcnt = max(maxcnt, cnt)
    if cnt not in counted:
        counted[cnt] = 1
    else:
        counted[cnt] += 1
print(maxcnt, counted[maxcnt])