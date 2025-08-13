from collections import deque
input = open(0).readline

DIFF = ((0, 1), (1, 0), (-1, 0), (0, -1))
queue = deque([])
# 미리 2차원 배열을 정의하고, 매 케이스 마다 h x w 크기로 덮어쓰며 사용한다.
visited = [[False for _ in range(100)] for _ in range(100)]
building = [["." for _ in range(100)] for _ in range(100)]

# 각 케이스 별 상태를 기록하는 변수
keys_have = {}
keys_available = {}
entrances = []
restart = False

# 상수
H = 0
W = 0

def bfs(R, C):
    # 진입 전 전처리
    tile = building[R][C]
    if (tile.isupper() and not keys_have.get(tile, False)) or visited[R][C] or tile == "*": # 벽이거나 기존에 방문한 경우 or 열쇠를 가지고 있지 않은 문
        return 0
    queue.append((R, C))
    visited[R][C] = True
    cnt = 0
    while queue:
        r, c = queue.popleft()
        for dr, dc in DIFF:
            nr = r + dr
            nc = c + dc
            if 0 <= nr < H and 0 <= nc < W and not visited[nr][nc]:
                # 타일 종류에 따라 처리하기
                tile = building[nr][nc]
                if tile.isalpha():
                    if tile.isupper() and keys_have.get(tile, False): # 열쇠를 가지고 있는 잠긴 문.
                        visited[nr][nc] = True
                        building[nr][nc] = "." # 영구적으로 열어둔다.
                        queue.append((nr, nc))
                    elif tile.islower(): # 열쇠
                        keys_have[tile.upper()] = True # 열쇠 획득
                        visited[nr][nc] = True
                        building[nr][nc] = "." # 이미 주운 열쇠는 맵에서 치운다.
                        global restart
                        restart = True
                        return cnt
                elif tile != "*":
                    if tile == "$":
                        cnt += 1
                    visited[nr][nc] = True
                    building[nr][nc] = "." # Prevent counting twice.
                    queue.append((nr, nc))

    return cnt

for _ in range(int(input())):
    H, W = map(int, input().split())
    cnt = 0
    building_str = [input().strip() for _ in range(H)]
    
    # 이미 가지고 있는 열쇠 등록하기
    keys = input().strip()
    if keys != "0":
        keys_have.update({k.upper(): True for k in keys})

    # 빌딩 지도 읽어오기 
    for r in range(H):
        for c, tile in enumerate(building_str[r]):
            building[r][c] = tile
            visited[r][c] = False
            if (r == 0 or r == H - 1 or c == 0 or c == W - 1) and tile != "*":
                if tile.isupper():
                    entrances.append((r, c)) # 일단 모든 문은 출입구로 고려해본다.
                elif tile.islower():
                    keys_have[tile.upper()] = True
                    building[r][c] = "."
                    entrances.append((r, c))
                else:
                    if tile == "$":
                        cnt += 1
                        building[r][c] = "."
                    entrances.append((r, c))
                    
            if tile.islower(): # 잠재적으로 얻을 수 있는 열쇠 기록해 두기
                keys_available[tile.upper()] = True
    # BFS
    idx = 0
    while idx < len(entrances):
        r, c = entrances[idx]
        cnt += bfs(r, c)
        idx += 1
        if restart:
            for r in range(H):
                for c in range(W):
                    visited[r][c] = False
            queue.clear()
            idx = 0
            restart = False

    print(cnt)

    # 상태변수 초기화
    queue.clear()
    keys_have.clear()
    keys_available.clear()
    entrances.clear()