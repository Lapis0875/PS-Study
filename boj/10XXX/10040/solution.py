input = open(0).readline
N, M = map(int, input().strip().split())
Cost = []
for idx in range(N):
    Cost.append((idx, int(input().strip())))
Judges = []
for idx in range(M):
    Judges.append(int(input().strip()))

votes = [0 for _ in range(N)]
max_vote = -1
for judge in Judges:
    max_fun = N
    for idx, cost in Cost:
        if cost > judge:
            continue
        if idx < max_fun:
            max_fun = idx
    votes[max_fun] += 1
    if max_fun != max_vote and votes[max_fun] > votes[max_vote]:
        max_vote = max_fun

print(Cost[max_vote][0] + 1)