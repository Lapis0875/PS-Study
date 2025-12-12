input = open(0).readline
INF = 100_001

def distance(r1, c1, r2, c2):
    """두 2차원 좌표의 맨해튼 거리(택시 거리)를 계산한다."""
    return abs(r1 - r2) + abs(c1 - c2)

N, M = map(int, input().split())
CITY = [[0] * N for _ in range(N)]

HOUSE_COORDS = []
CHICKEN_COORDS = []
for r in range(N):
    for c, v in enumerate(map(int, input().split())):
        CITY[r][c] = v
        if v == 1:
            HOUSE_COORDS.append((r, c))
        elif v == 2:
            CHICKEN_COORDS.append([r, c, True])

CHICKEN_REMOVE = len(CHICKEN_COORDS) - M

# 풀이 과정
# 1. M개의 치킨집을 제외한 나머지 칸을 빈칸으로 처리
# 2. 해당 상태의 도시의 치킨 거리 구하기
# 3. 도시의 치킨 거리의 최솟값 구하기

# 2. 현재 도시의 상태를 기반으로 도시의 치킨 거리 계산하기
def calc_city_distance():
    """현재 도시의 치킨 거리 계산하기"""
    dist = 0
    for home_r, home_c in HOUSE_COORDS:
        cur_dist = INF
        for chicken_r, chicken_c, flag in CHICKEN_COORDS:
            if flag: # 현재 남아있는 치킨집에 대해서만 거리 계산
                cur_dist = min(cur_dist, distance(home_r, home_c, chicken_r, chicken_c))
        dist += cur_dist
                
    return dist

# 1. M개의 치킨집만 남기고 다 빈칸으로 치우기
min_dist = INF

def dfs(depth, next_idx):
    """백트래킹으로 치킨집을 M개만 남기고 지우기"""
    if depth == CHICKEN_REMOVE: 
        # 3. 도시의 치킨 거리의 최솟값 구하기.
        global min_dist
        min_dist = min(min_dist, calc_city_distance())
        return
    
    for i in range(next_idx, len(CHICKEN_COORDS)): # 이전에 탐색한 지점의 이후부터 탐색해야 중복되는 경우를 제외할 수 있다.
        r = CHICKEN_COORDS[i][0]
        c = CHICKEN_COORDS[i][1]
        if CITY[r][c] != 2:
            continue
        CITY[r][c] = 0
        CHICKEN_COORDS[i][2] = False
        dfs(depth + 1, i + 1)
        CITY[r][c] = 2
        CHICKEN_COORDS[i][2] = True

dfs(0, 0)
print(min_dist)
