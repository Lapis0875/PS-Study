from sys import stdin
from collections import deque
from typing import Callable, Literal

N: int = int(stdin.readline())

stk: deque[int] = deque()

def push(x: int) -> None:
    stk.appendleft(x)

def pop() -> int:
    return stk.popleft() if stk else -1

def count() -> int:
    return len(stk)

def empty() -> Literal[1, 0]:
    return 0 if stk else 1

def top() -> int:
    return stk[0] if stk else -1

cmd_map: dict[str, Callable[[], int]] = {
    "2": pop,
    "3": count,
    "4": empty,
    "5": top
} 

for _ in range(N):
    line: str = stdin.readline()[:-1]
    if line[0] == "1":
        _, x = line.split()
        push(int(x))
    else:
        print(cmd_map[line[0]]())
