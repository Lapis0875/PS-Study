input = open(0).readline
N, M = map(int, input().split())
collect = list(map(int, input().split()))
spy = list(map(int, input().split()))

PLACE = 0
MISSION = 1
EMPTY = -1
COLLECT_MISSION = 0
SPY_MISSION = 1

count = 0
course = [[EMPTY, EMPTY] for _ in range(N)]
def dfs(depth, progress):
    if depth == N:
        if progress >= M:
            global count
            count += 1
        return
    
    for i in range(3):
        course[depth][PLACE] = i
        course[depth][MISSION] = COLLECT_MISSION
        dfs(depth + 1, progress + (collect[i] // 2 if depth > 0 and course[depth - 1][0] == i else collect[i]))
        course[depth][MISSION] = SPY_MISSION
        dfs(depth + 1, progress + (spy[i] // 2 if depth > 0 and course[depth - 1][0] == i else spy[i]))
        course[depth][PLACE] = EMPTY
        course[depth][MISSION] = EMPTY

dfs(0, 0)
print(count)
