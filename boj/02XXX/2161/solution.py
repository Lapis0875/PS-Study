from sys import stdin
from collections import deque

N: int = int(stdin.readline())
queue: deque[int] = deque(range(1, N + 1))
dropped: list[int] = []

while len(queue) > 1:
    dropped.append(queue.popleft())     # 제일 윗 장의 카드를 버린다.
    queue.append(queue.popleft())       # 다음번 윗 장의 카드는 제일 아래에 깐다.

dropped.append(queue.pop())

print(" ".join(map(str, dropped)))
