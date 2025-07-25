from sys import stdin

N: int = int(stdin.readline())

arr: list[int] = [-1 for _ in range(N + 1)]
graph: list[list[int]] = [[] for _ in range(N + 1)]
prerequisites: list[list[int]] = [[] for _ in range(N + 1)]
for i in range(1, N + 1):
    base, *pre = map(int, stdin.readline().split())
    arr[i] = base
    for x in pre:
        graph[i].append(x)
    prerequisites[i].extend(pre)

for i, pre in enumerate(prerequisites[1:], 1):
    if len(pre) != 1:
        while pre[0] != -1:
            req: int = pre.pop(0)
            

for x in arr[1:]:
    print(x)