from itertools import combinations
from functools import reduce

input = open(0).readline
N, M = map(int, input().split())
primes = list(map(int, input().split()))

res = 0
for i in range(1, N + 1):
    for comb in combinations(primes, i):
        base = reduce(lambda e, s: e * s, comb)
        cnt = M // base
        if i % 2: # Substract if odd
            res += cnt
        else: # Add if even
            res -= cnt

print(res)
