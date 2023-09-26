from collections import deque
from sys import stdin
from typing import Callable

N: int = int(stdin.readline())
deq: deque[int] = deque()

def push_front(x: int) -> None:
    deq.appendleft(x)

def push_back(x: int) -> None:
    deq.append(x)

cmd_map: dict[str, Callable[[], None]] = {
    "3": lambda: print(deq.popleft() if deq else -1),
    "4": lambda: print(deq.pop() if deq else -1),
    "5": lambda: print(len(deq)),
    "6": lambda: print(0 if deq else 1),
    "7": lambda: print(deq[0] if deq else -1),
    "8": lambda: print(deq[-1] if deq else -1),
}

for _ in range(N):
    cmd: str = stdin.readline()[:-1]
    if cmd.startswith("1"):
        push_front(int(cmd.split()[1]))
    elif cmd.startswith("2"):
        push_back(int(cmd.split()[1]))
    else:
        cmd_map[cmd]()
