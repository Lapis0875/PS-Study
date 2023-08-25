from sys import stdin
from collections import deque

N, K = map(int, stdin.readline().split())

queue: deque[int] = deque(range(1, N + 1))
count: int = 0

# 1 2 [3] 4 5 6 7 --> 4 5 [6] 7 1 2 --> 7 1 [2] 4 5 --> 4 5 [7] 1 --> 1 4 [5] --> [1] 4 --> [4]
        
print("<", end="")
for _ in range(N):
    for _ in range(K - 1):
        queue.append(queue.popleft())
    count += 1
    print(queue.popleft(), end="")
    if count < N:
        print(", ", end="")
print(">")