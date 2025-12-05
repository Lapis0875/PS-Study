input = open(0).readline

N = int(input())
index_map = [[0, False] for _ in range(2001)]
max_value = 0
for i, v in enumerate(map(int, input().split())):
    if not index_map[v][1]: # 첫 번째 인덱스 입력
        index_map[v][0] = i
        index_map[v][1] = True
    else: # 두 번째 인덱스 입력
        index_map[v][0] = abs(index_map[v][0] - i) - 1
        max_value = max(max_value, index_map[v][0])

print(max_value)