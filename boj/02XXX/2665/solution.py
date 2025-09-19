# https://www.acmicpc.net/problem/2665
from heapq import heappop, heappush
input = open(0).readline
N = int(input())
# 구현의 편의를 위해, 흰 방을 0으로 두고 검은 방을 1로 둔다 (입력을 반전시킴)
room = list(list(map(lambda x: 1 - int(x), input().rstrip())) for _ in range(N)) # type: list[list[Literal[0, 1]]]

# (0, 0) -> (N - 1, N - 1)로 가는 최단 거리를 찾기. 단, 흰 방만 지나갈 수 있으며, 검은 방은 흰 방으로 바꾼 뒤 지나갈 수 있다.
# 검은 방을 흰 방으로 바꾼 횟수가 최소가 되는 경로 찾기

# Idea.
# 1. 검은방 흰방 상관없이 격자 그래프 상에서 그래프 탐색 진행하기
# 2-1. 만약 검은 방을 방문했다면, 바꾼 방 개수를 1 증가시킴 (방문한 검은 방의 개수를 기억하자)
# 2-2. "방문한 검은 방의 개수"를 가중치로 갖는 우선순위 큐를 활용한 너비 우선 탐색을 진행 -> 검은 방을 최소한으로 방문한 결과를 제일 먼저 도출해낸다.
# 3. 2에서 구한 검은 방의 개수가 최소가 되는 경우를 찾는다. 이게 답.

MAX = N * N
DIFF = ((-1, 0), (1, 0), (0, -1), (0, 1))
visited = [[False] * N for _ in range(N)]
distance = [[MAX] * N for _ in range(N)]
distance[0][0] = 0
queue = []
heappush(queue, (0, 0, 0))

while queue:
    cost, r, c = heappop(queue)
    for dr, dc in DIFF:
        nr = r + dr
        nc = c + dc
        if 0 <= nr < N and 0 <= nc < N and not visited[nr][nc]:
            visited[nr][nc] = True
            new_dist = cost + room[nr][nc] # 검은 방이면 1 증가, 그렇지 않으면 이전 거리와 동일
            if new_dist < distance[nr][nc]:
                distance[nr][nc] = new_dist
                heappush(queue, (new_dist, nr, nc))

print(distance[N-1][N-1])
