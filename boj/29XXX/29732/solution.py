input = open(0).readline
N, M, K = map(int, input().split())
INFECTED = "R"
NOT_INFECTED = "."
people = input().rstrip()
after = [people[i] == INFECTED for i in range(N)]

cnt = 0
for i in range(N):
    if people[i] == NOT_INFECTED:
        continue
    for j in range(max(0, i - K), min(N, i + K + 1)):
        after[j] = True

for i in range(N):
    if after[i]:
        cnt += 1
print("Yes" if cnt <= M else "No")