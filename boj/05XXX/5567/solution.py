from collections import deque
input = open(0).readline
N = int(input())
friends = tuple([] for _ in range(N + 1))
visited = [-1] * (N + 1) # -1: 방문 X(친구가 아님), 0: 자기 자신, 1: 친구, 2: 친구의 친구 (자신으로부터 몇칸 떨어져 연결되는지를 찾는다.)
for _ in range(int(input())):
    a, b = map(int, input().split())
    friends[a].append(b)
    friends[b].append(a)

queue = deque([1])
visited[1] = 0
while queue:
    cur = queue.popleft()
    for friend in friends[cur]:
        if visited[friend] == -1:
            visited[friend] = visited[cur] + 1
            queue.append(friend)

cnt = 0
for i in range(2, N + 1):
    if 0 < visited[i] <= 2:
        cnt += 1
print(cnt)