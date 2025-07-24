input = open(0).readline
N, S = map(int, input().split())

NOT_VISITED = N * 2 # 방문하지 않은 정점임을 표시할 적절한 수
DP = [{} for _ in range(N + 1)]
DP[1][1] = 0
DP[2][1] = 1

cannot_pass = {}
for _ in range(S):
    cannot_pass[int(input())] = True

for i in range(2, N):
    if cannot_pass.get(i):
        continue
    # print(f"[ i = {i} ]")
    for cur_speed in DP[i].keys():
        for next_speed in (cur_speed - 1, cur_speed, cur_speed + 1):
            next_stone = i + next_speed
            if i < next_stone <= N and not cannot_pass.get(next_stone, False):
                # print(f"-> next = {next_stone}, jumps = {DP[i][cur_speed] + 1}, speed = {next_speed}")
                DP[next_stone][next_speed] = min(DP[next_stone].get(next_speed, NOT_VISITED), DP[i][cur_speed] + 1)

print(min(DP[N].values()) if len(DP[N]) > 0 else -1)