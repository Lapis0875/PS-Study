from collections import deque
from sys import stdin

Location = tuple[int, int, int, int]                 # (x, y, h, days)
M, N, H = map(int, stdin.readline().split())
box: list[list[list[int]]] = []
initial: list[Location] = []
counter: dict[int, int] = {-1: 0, 0: 0, 1: 0}

for h in range(H):
    floor: list[list[int]] = []
    for y in range(N):
        line: list[int] = []
        for x, t in enumerate(map(int, stdin.readline().split())):    # t is tomato
            line.append(t)
            counter[t] += 1
            if t == 1:
                initial.append((x, y, h, 0))
        floor.append(line)
    box.append(floor)

if counter[0] == 0:
    print(0)
else:
    q: deque[Location] = deque(initial)
    d: int = 0
    while q:
        x, y, h, d = q.popleft()
        t: int = box[h][y][x]
        if t == 1:        # 자신과 인접한 타일을 익게 만든다.
            if x >= 1 and box[h][y][x - 1]  == 0:
                box[h][y][x - 1] = 1
                counter[0] -= 1
                counter[1] += 1
                q.append((x - 1, y, h, d + 1))
            if x <= M - 2 and box[h][y][x + 1] == 0:
                box[h][y][x + 1] = 1
                counter[0] -= 1
                counter[1] += 1
                q.append((x + 1, y, h, d + 1))
            if y >= 1 and box[h][y - 1][x] == 0:
                box[h][y - 1][x] = 1
                counter[0] -= 1
                counter[1] += 1
                q.append((x, y - 1, h, d + 1))
            if y <= N - 2 and box[h][y + 1][x] == 0:
                box[h][y + 1][x] = 1
                counter[0] -= 1
                counter[1] += 1
                q.append((x, y + 1, h, d + 1))
            if h >= 1 and box[h - 1][y][x] == 0:
                box[h - 1][y][x] = 1
                counter[0] -= 1
                counter[1] += 1
                q.append((x, y, h - 1, d + 1))
            if h <= H - 2 and box[h + 1][y][x] == 0:
                box[h + 1][y][x] = 1
                counter[0] -= 1
                counter[1] += 1
                q.append((x, y, h + 1, d + 1))
    if counter[0] > 0:
        print(-1)
    else:
        print(d)