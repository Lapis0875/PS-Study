from collections import deque
from sys import stdin

Location = tuple[int, int, int]                 # (x, y, days)
M, N = map(int, stdin.readline().split())
box: list[list[int]] = []
initial: list[Location] = []
counter: dict[int, int] = {-1: 0, 0: 0, 1: 0}

for y in range(N):
    line: list[int] = []
    for x, t in enumerate(map(int, stdin.readline().split())):    # t is tomato
        line.append(t)
        counter[t] += 1
        if t == 1:
            initial.append((x, y, 0))
    box.append(line)

if counter[0] == 0:
    print(0)
else:
    q: deque[Location] = deque(initial)
    d: int = 0
    while q:
        x, y, d = q.popleft()
        t: int = box[y][x]
        if t == 1:        # 자신과 인접한 타일을 익게 만든다.
            if x >= 1:
                t2 = box[y][x - 1]
                if t2 == 0:
                    box[y][x - 1] = 1
                    counter[0] -= 1
                    counter[1] += 1
                    q.append((x - 1, y, d + 1))
            if x <= M - 2:
                t2 = box[y][x + 1]
                if t2 == 0:
                    box[y][x + 1] = 1
                    counter[0] -= 1
                    counter[1] += 1
                    q.append((x + 1, y, d + 1))
            if y >= 1:
                t2 = box[y - 1][x]
                if t2 == 0:
                    box[y - 1][x] = 1
                    counter[0] -= 1
                    counter[1] += 1
                    q.append((x, y - 1, d + 1))
            if y <= N - 2:
                t2 = box[y + 1][x]
                if t2 == 0:
                    box[y + 1][x] = 1
                    counter[0] -= 1
                    counter[1] += 1
                    q.append((x, y + 1, d + 1))
    if counter[0] > 0:
        print(-1)
    else:
        print(d)