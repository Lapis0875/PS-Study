input = open(0).readline
N = int(input())

width = 2
for _ in range(N):
    width = 2 * width - 1

print(width ** 2)