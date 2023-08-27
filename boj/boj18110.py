from decimal import Decimal, ROUND_HALF_UP
from sys import stdin
from typing import Final

ZERO = Decimal("0.")

def round(n: float) -> int:
    return Decimal(n).quantize(ZERO, rounding=ROUND_HALF_UP)

N: Final[int] = int(stdin.readline())
if N == 0:
    print(0)
else:
    ratings: list[int] = sorted(int(stdin.readline()) for _ in range(N))

    removalCnt: int = int(round(N * 0.15))
    if removalCnt != 0:
        ratings = ratings[removalCnt:-removalCnt]
    print(round(sum(ratings) / (N - 2 * removalCnt)))
