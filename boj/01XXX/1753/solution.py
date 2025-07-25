from queue import PriorityQueue

INF = 100_000_001
input = open(0).readline
V, E = map(int, input().split())    # 정점의 개수, 간선의 개수
K = int(input().strip())            # 시작 정점 번호
graph = [[] for _ in range(V + 1)]  # 그래프 초기화
for _ in range(E):
    u, v, w = map(int, input().split())
    graph[u].append((v, w))              # u에서 v로 가는 간선과 가중치 추가 (주어진 그래프는 방향 그래프이므로 u->v로만 간선 추가)

distance = [INF for _ in range(V + 1)]
distance[K] = 0
pq = PriorityQueue()  # 우선순위 큐 초기화
pq.put((0, K))
while not pq.empty():
    dist, current_node = pq.get()  # 현재 노드와 거리를 가져옴
    if distance[current_node] < dist:  # 이미 더 짧은 경로가 있는 경우
        continue
    for neighbor, weight in graph[current_node]:  # 현재 노드의 이웃 노드와 가중치 확인
        new_distance = dist + weight
        if new_distance < distance[neighbor]:  # 새로운 거리가 더 짧은 경우
            distance[neighbor] = new_distance
            pq.put((new_distance, neighbor))

print("\n".join(map(lambda x: str(x) if x < INF else "INF", distance[1:])))