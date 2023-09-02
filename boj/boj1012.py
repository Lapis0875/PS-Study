from sys import stdin, setrecursionlimit

Location = tuple[int, int]            # (x, y)
setrecursionlimit(10 ** 6)
T: int = int(stdin.readline())

def DFS(x: int, y: int, M: int, N: int, K: int, farm: list[list[int]]) -> bool:
    before: int = farm[y][x]
    if farm[y][x] == 0:
        # 방문 처리
        farm[y][x] = 1
        # 인접한 상추로 DFS
        if x >= 1:
            DFS(x - 1, y, M, N, K, farm)
        if x <= M - 2:
            DFS(x + 1, y, M, N, K, farm)
        if y >= 1:
            DFS(x, y - 1, M, N, K, farm)
        if y <= N - 2:
            DFS(x, y + 1, M, N, K, farm)
    return farm[y][x] != before

for _ in range(T):
    M, N, K = map(int, stdin.readline().split())
    lettuces: list[Location] = []
    for _ in range(K):
        x, y = map(int, stdin.readline().split())
        lettuces.append((x, y))
    farm = [[-1 for _ in range(M)] for _ in range(N)]
    for lettuce in lettuces:
        x, y = lettuce
        farm[y][x] = 0
    
    count: int = 0
    for lettuce in lettuces:                            # 전체 상추 목록에 대해 DFS
        x, y = lettuce
        res = DFS(x, y, M, N, K, farm)     # 이미 방문했던 상추를 다시 루트로 잡고 DFS 할 경우, False를 반환해 개수에 반영 X
        # print(f"\n>>> DFS({x}, {y}) : {res}")
        count += res
        # for line in farm:
        #     for tile in line:
        #         if tile == -1:
        #             print(f"[ X ] ", end="")
        #         elif tile == 0:
        #             print(f"[ O ] ", end="")
        #         else:
        #             print(f"[ @ ] ", end="")
        #     print()

    print(count)
