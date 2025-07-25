input = open(0).readline
target = [[[0, 0, 0] for _ in range(6)] for _ in range(4)]

for i in range(4):
    line = input().split(" ")
    for j in range(6):
        target[i][0] = line[3*j + 0]
        target[i][1] = line[3*j + 1]
        target[i][2] = line[3*j + 2]

# 대진표 구성하기
games = []
for i in range(5):
    for j in range(i + 1, 6):
        games.append((i, j))

worldcup_result = [[0, 0, 0] for _ in range(6)]
check = [False for _ in range(4)]
def dfs(depth):
    print(f"[{depth}] {worldcup_result}")
    if depth == 15: # 15개 경기를 모두 마치고 나면 결과 정산
        for i in range(4):
            for j in range(6):
                if not check[i] and all(target[i][j][k] == worldcup_result[j][k] for k in range(3)):
                    print(">>> Found Case {i}!")
                    return
        print(">>> No Matching Cases in this route.")
        return
    
    i, j = games[depth]
    # 3가지 경우의 수 백트래킹
    # i 승리, j 패배
    # i 패배, j 승리
    # 무승부
    for a, b in ((0, 2), (2, 0), (1, 1)):
        worldcup_result[i][a] += 1
        worldcup_result[j][b] += 1
        if sum(worldcup_result[i]) <= 5 and sum(worldcup_result[j]) <= 5:
            dfs(depth + 1)
        worldcup_result[i][a] -= 1
        worldcup_result[j][b] -= 1

dfs(0)
print(" ".join(map(lambda r: "1" if r else "0", check)))