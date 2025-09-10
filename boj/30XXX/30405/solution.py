input = open(0).readline

N, M = map(int, input().split())

entrances = []

for i in range(N):
    k, start, *_, end = map(int, input().split())
    entrances.append(start)
    entrances.append(end)

entrances.sort()

print(entrances[N - 1])