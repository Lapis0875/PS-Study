input = open(0).readline
INF = 100_001
N, M = map(int, input().split())
CITY = [list(map(int, input().split())) for _ in range(N)]

houses = []
chickens = []
for y in range(N):
    for x in range(N):
        if CITY[y][x] == 1:
            houses.append((y, x))
        elif CITY[y][x] == 2:
            chickens.append((y, x))

distance = [INF for _ in range(len(houses))]
visited = [False for _ in range(len(chickens))]
prev = [INF for _ in range(len(houses))]
result = 100_000_000


steps = [[0 for _ in range(len(houses))] for _ in range(M)]
def debug_print(depth):
    global result, visited, distance, houses
    print(f"[depth = {depth}, result = {result}]")
    print(f"visited: ")
    tiles = [["X" for _ in range(N)] for _ in range(N)]
    for i, v in enumerate(visited):
        if v:
            cy, cx = chickens[i]
            tiles[cy][cx] = "O"
    print("\n".join(" ".join(row) for row in tiles))
    print(f"\ndistance: ")
    for i, d in enumerate(distance):
        print(f"houses[{i}] {houses[i]} = {d}")
    print(f"\nsteps: ")
    for i, cur_step in enumerate(steps):
        print(f"steps[{i}]\n")
        for step_distance in cur_step:
            print(f"  - {step_distance}")
    print("---\n")

def debug_steps(depth):
    global steps
    for i, d in enumerate(distance):
        steps[depth][i] = d

def dfs(depth):
    if depth == M:
        global result
        cur = sum(distance)
        if cur < result:
            print(f"최솟값 갱신 {result} -> {cur}")
        result = min(result, cur)
        debug_print(depth)
        return

    for i in range(len(chickens)):
        if not visited[i]:
            cy, cx = chickens[i]
            visited[i] = True
            for j in range(len(houses)):
                prev[j] = distance[j]
                distance[j] = min(distance[j], abs(houses[j][0] - cy) + abs(houses[j][1] - cx))
            debug_steps(depth)
            dfs(depth + 1)
            visited[i] = False
            for j in range(len(houses)):
                distance[j] = prev[j]

dfs(0)
print(result)