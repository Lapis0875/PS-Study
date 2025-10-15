input = open(0).readline
N, M = map(int, input().split())

graph = []

for _ in range(N):
    graph.append(list(map(int, input().split())))

for mid in range(N):
    for i in range(N):
        for j in range(N):
            if graph[i][mid] + graph[mid][j] < graph[i][j]:
                graph[i][j] = graph[i][mid] + graph[mid][j]

for _ in range(M):
    a, b, c = map(int, input().split())
    # 정점 번호를 0~N-1 로 사용
    print("Enjoy other party" if graph[a - 1][b - 1] <= c else "Stay here")
