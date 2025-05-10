from sys import stdin
from collections import deque

N, K, M = map(int, stdin.readline().split())
deq = deque(i for i in range(1, N + 1))

cnt = 0
reverse = False
while deq:
    cnt += 1
    deq.rotate(K if reverse else -K + 1)    # K번째 값을 가져오려면 K-1만큼 회전해야 함. 오른쪽으로 회전하려면 -방향으로 회전해야 함.
    # print(deq)
    print(deq.popleft())
    if cnt % M == 0:
        reverse = not reverse

