from heapq import heappush, heappop

input = open(0).readline
N = int(input())

visited = {N: 0}
queue = []
heappush(queue, (0, N))
while queue:
    tries, x = heappop(queue)
    if x == 1:
        print(visited[1])
        break
    # 1. x / 3
    if x % 3 == 0:
        next_x = x // 3
        if not next_x in visited:
            visited[next_x] = tries + 1
            heappush(queue, (visited[next_x], next_x))
    # 2. x / 2
    if x % 2 == 0:
        next_x = x // 2
        if not next_x in visited:
            visited[next_x] = tries + 1
            heappush(queue, (visited[next_x], next_x))
    # 3. x - 1
    next_x = x - 1
    if not next_x in visited:
        visited[next_x] = tries + 1
        heappush(queue, (visited[next_x], next_x))