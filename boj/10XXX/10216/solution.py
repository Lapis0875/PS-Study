input = open(0).readline
enemy_base = [None] * 3000
roots = [i for i in range(3000)]
base_cnt = 0

# Union - Find

def find_root(x):
    path = []
    while x != roots[x]:
        path.append(x)
        x = roots[x]

    for p in path:
        roots[p] = x
    
    return x

def union(x, y):
    x = find_root(x)
    y = find_root(y)

    if x == y:
        return False # 이미 같은 집합

    # 더 작은 수를 루트 노드로 정함
    if x > y:
        roots[x] = y
    else:
        roots[y] = x
    
    return True

def is_connected(i, j):
    d2 = (enemy_base[i][0] - enemy_base[j][0]) ** 2 + (enemy_base[i][1] - enemy_base[j][1]) ** 2
    R2 = (enemy_base[i][2] + enemy_base[j][2]) ** 2
    return d2 <= R2

for _ in range(int(input())):
    N = int(input())

    for i in range(N):
        roots[i] = i
        enemy_base[i] = tuple(map(int, input().split())) # (x, y, R)
    
    for i in range(N):
        for j in range(N):
            if i != j and is_connected(i, j):
                union(i, j)
    
    base_cnt = 0
    for i in range(N):
        if roots[i] == i:
            base_cnt += 1

    print(base_cnt)
    
