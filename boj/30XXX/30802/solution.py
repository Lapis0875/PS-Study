input = open(0).readline
N = int(input())
SIZE = list(map(int, input().strip().split()))
T, P = map(int, input().split())

t_pairs = 0
for s in SIZE:
    t_pairs += s // T
    if s % T != 0:
        t_pairs += 1

print(f"{t_pairs}\n{N // P} {N % P}")