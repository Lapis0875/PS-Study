from heapq import heappop, heappush
input = open(0).readline
barn = [[0] * 10 for _ in range(10)]
DIRECTIONS = ((-1, 0), (1, 0), (0, -1), (0, 1))
queue = []
for r in range(10):
    for c, t in enumerate(input().rstrip()):
        if t == "B":
            barn[r][c] = 1
            heappush(queue, (0, r, c))
        elif t == "R":
            barn[r][c] = 2
        elif t == "L":
            barn[r][c] = 3
        else:
            barn[r][c] = 0

while queue:
    dist, r, c = heappop(queue)
    for dr, dc in DIRECTIONS:
        nr = r + dr
        nc = c + dc

        if 0 <= nr < 10 and 0 <= nc < 10 and barn[nr][nc] != 2 and barn[nr][nc] != -1:
            if barn[nr][nc] == 3:
                print(dist)
                queue.clear()
            barn[nr][nc] = -1  # 방문 처리
            heappush(queue, (dist + 1, nr, nc))