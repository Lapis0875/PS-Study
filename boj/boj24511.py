from sys import stdin
from collections import deque

N: int = int(stdin.readline())

queuestack: deque[int] = deque()
where_is_queue: list[bool] = list(map(lambda x: x == "0", stdin.readline().split()))
for i, v in enumerate(map(int, stdin.readline().split())):
    if where_is_queue[i]:
        queuestack.append(v)

M: int = int(stdin.readline())
arr: list[int] = list(map(int, stdin.readline().split()))

for i in arr:
    queuestack.appendleft(i)
for i in range(M):
    print(queuestack.pop(), end=" " if i < M - 1 else "\n")
