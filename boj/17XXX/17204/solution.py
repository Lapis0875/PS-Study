input = open(0).readline
N, K = map(int, input().split())
arr = [-1] * N
visited = [False] * N

for i in range(N):
    arr[i] = int(input())

n = 0
visited[0] = True
cnt = 0
while n != K:
    cnt += 1
    n = arr[n]
    if visited[n]: # 사이클 발생, 이후엔 계속 같은 사람을 지목하게 됨.
        print(-1)
        break
    visited[n] = True
else:
    print(cnt)