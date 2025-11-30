input = open(0).readline
N, M = map(int, input().split())

def distance(point1, point2):
    dist = 0
    for i in range(N):
        dist += abs(point1[i] - point2[i])
    return dist

points = list(tuple(map(int, input().split())) for _ in range(M))

# 맨해튼 거리의 계산 식에서, 서로 다른 차원의 원소는 거리 계산에 영향을 주지 못한다. (독립적)
# 따라서, 찾고자 하는 지점은 M개의 점의 각 차원별 중앙값으로 구성된다.
pos = [0] * N
for i in range(N):
    coords = sorted(points, key=lambda x: x[i])
    pos[i] = coords[(M - 1) // 2][i] # 항상 중앙값을 찾는다. M이 홀수라면 중앙값은 1개이고, 짝수라면 중앙값은 2개이나 둘 다 중앙값이므로 어느 것을 택해도 결과는 같다.
    
dist = 0
for i in range(M):
    dist += distance(points[i], pos)

print(dist)
print(*pos)