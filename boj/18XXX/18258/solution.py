# Migrated from ./boj/boj18258.py by boj_validator
from collections import deque
from sys import stdin
from typing import Callable

N: int = int(stdin.readline())
queue: deque[int] = deque()

def push(x: int) -> None:
    queue.append(x)

def pop() -> None:
    print(queue.popleft() if queue else -1)

def size() -> None:
    print(len(queue))

def empty() -> None:
    print(0 if queue else 1)

def front() -> None:
    print(queue[0] if queue else -1)

def back() -> None:
    print(queue[-1] if queue else -1)

cmd_map: dict[str, Callable[[], None]] = {
    "pop": pop,
    "size": size,
    "empty": empty,
    "front": front,
    "back": back
}

for _ in range(N):
    cmd: str = stdin.readline()[:-1]
    if cmd.startswith("push"):
        push(int(cmd.split()[1]))
    else:
        cmd_map[cmd]()
