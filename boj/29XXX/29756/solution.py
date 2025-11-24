input = open(0).readline
N, K = map(int, input().split())
S = list(map(int, input().split()))
H = list(map(int, input().split()))
DP = [[-1 for _ in range(101)] for _ in range(N + 1)]
DP[0][100] = 0 # Only available start point.

for i in range(1, N + 1):
    for h in range(101):
        if DP[i - 1][h] == -1: # This isn't valid case.
            continue

        # In every section, player's hp is healed first.
        after_heal = min(h + K, 100)
        
        # Case 1) Skip this section.
        DP[i][after_heal] = max(DP[i][after_heal], DP[i - 1][h]) # healed.

        # Case 2) Play this section.
        if after_heal >= H[i - 1]:
            played_health = after_heal - H[i - 1]
            DP[i][played_health] = max(DP[i][played_health], S[i - 1] + DP[i - 1][h])

print(max(DP[N]))