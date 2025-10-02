input = open(0).readline
N = int(input())
stats = [list(map(int, input().split())) for _ in range(N)]

group = [False for _ in range(N)]
teams = [-1 for _ in range(N // 2)]
min_diff = float("inf")

def backtrack(depth, member_start, team1_stat):
    if depth == N // 2:
        global min_diff
        team2 = [i for i in range(N) if not group[i]]
        team2_stat = 0
        for player in team2:
            for other in team2:
                if player != other:
                    team2_stat += stats[player][other]
        
        diff = abs(team1_stat - team2_stat)
        min_diff = min(min_diff, diff)
        return
    
    original_stat = team1_stat
    for i in range(member_start, N):
        if not group[i]:
            group[i] = True
            teams[depth] = i
            for j in range(depth):
                team1_stat += stats[i][teams[j]] + stats[teams[j]][i]
            backtrack(depth + 1, i + 1, team1_stat)
            team1_stat = original_stat
            group[i] = False
            teams[depth] = -1

backtrack(0, 0, 0)
print(min_diff)