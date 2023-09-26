from sys import stdin
from collections import deque
from typing import Final, Literal

N: Final[int] = int(stdin.readline())
skills: str = stdin.readline()[:-1]

RStack: deque[Literal["L"]] = deque()
KStack: deque[Literal["S"]] = deque()

count: int = 0
for skill in skills:
    if skill == "R":
        if RStack and RStack.popleft() == "L":
            count += 1
        else:
            break
    elif skill == "K":
        if KStack and KStack.popleft() == "S":
            count += 1
        else:
            break
    elif skill == "L":
        RStack.append(skill)
    elif skill == "S":
        KStack.append(skill)
    elif "1" <= skill <= "9":
        count += 1

print(count)
