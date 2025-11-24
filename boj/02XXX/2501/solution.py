from math import sqrt
input = open(0).readline
N, K = map(int, input().split())

divisors = [1, N]
for i in range(2, int(sqrt(N)) + 1):
    if N % i == 0:
        divisors.append(i)
        other = N // i
        if other != i:
            divisors.append(other)

divisors.sort()
print(divisors[K - 1] if len(divisors) >= K else 0)