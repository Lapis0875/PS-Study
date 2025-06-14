from collections import deque
input = open(0).readline
A, B = map(int, input().strip().split())
if A == B:
    print(0)
    exit(0)
N, M = map(int, input().strip().split())

adj_list: list[list[int]] = [[] for _ in range(N + 1)]  # 1번 인덱스부터 쓰기 위해 크기 + 1
for _ in range(M):
    u, v = map(int, input().strip().split())
    adj_list[u].append(v)
    adj_list[v].append(u)

queue = deque([A])
check = [0 for _ in range(N + 1)]
while queue:
    x = queue.popleft()
    for n in adj_list[x]:
        if check[n] == 0:
            queue.append(n)
            check[n] = check[x] + 1

print(check[B] or -1)
