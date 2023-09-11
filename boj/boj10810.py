from sys import stdin

N, M = map(int, stdin.readline().split())
baskets: list[int] = [0] * (N + 1)


for _ in range(M):
    i, j, k = map(int, stdin.readline().split())
    for n in range(i, j + 1):
        baskets[n] = k

print(" ".join(map(str, baskets[1:])))
