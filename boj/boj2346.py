from sys import stdin
from collections import deque

N: int = int(stdin.readline())
deq: deque[tuple[int, int]] = deque()

for i, x in enumerate(map(int, stdin.readline().split()), 1):
    deq.append((i, x))  # (index, value)


res: list[int] = []
while deq:
    index, value = deq.popleft()
    res.append(index)
    
    if deq:
        if value > 0:
            for _ in range(value - 1):
                deq.append(deq.popleft())
        else:
            for _ in range(-value):
                deq.appendleft(deq.pop())

print(" ".join(map(str, res)))
