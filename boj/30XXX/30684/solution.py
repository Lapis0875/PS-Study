input = open(0).readline
N = int(input())

candidates = []

for _ in range(1, N):
    name = input().strip()
    if len(name) == 3:
        candidates.append(name)
candidates.sort()
print(candidates[0])