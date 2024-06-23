from sys import stdin
from typing import Final, Literal

N: Final[int] = int(stdin.readline())
have: list[int] = sorted(map(int, stdin.readline().split()))
M: Final[int] = int(stdin.readline())
cards: tuple[int, ...] = tuple(map(int, stdin.readline().split()))

def bisect(left: int, right: int, key: int) -> Literal["0", "1"]:
    mid: int = (left + right) // 2
    if have[mid] == key:
        return "1"
    elif have[mid] > key:
        return bisect(left, mid - 1, key) if left < mid else "0"
    else:
        return bisect(mid + 1, right, key) if mid < right else "0"

answer: list[str] = []
for card in cards:
    answer.append(bisect(0, N - 1, card))
print(" ".join(answer))