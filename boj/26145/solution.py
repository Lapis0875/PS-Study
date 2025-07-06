input = open(0).readline
N, M  = map(int, input().split())
S = list(map(int, input().split()))
Total = [0 for _ in range(N + M)]

for i in range(N):
    for j, t in enumerate(map(int, input().split())):
        Total[j] += t
        S[i] -= t

for i in range(N):
    Total[i] += S[i]

print(" ".join(map(str, Total)))