input = open(0).readline

N = int(input())
ropes = sorted((int(input()) for _ in range(N)), reverse=True)

max_weight = ropes[0]
for i in range(1, N):
    weight = ropes[i] * (i + 1) # K개의 로프를 병렬 연결했을 때, 그 중 최소 하중을 M이라 하면 이 병렬 연결이 견딜 수 있는 최대 하중은 K x M
    if weight > max_weight:
        max_weight = weight
print(max_weight)
