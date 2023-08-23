from math import sqrt
from sys import stdin

M = int(stdin.readline())
N = int(stdin.readline())

sieve: list[int] = [ False, False ]
sieve.extend(True for _ in range(2, N + 1))

for i in range(2, int(sqrt(N)) + 1):
    if sieve[i]:
        j: int = 2
        while (x := i * j) <= N:
            sieve[x] = False
            j += 1

primes = [i for i in range(M, N + 1) if sieve[i]]
        
if len(primes) == 0:
    print(-1)
else:
    print(sum(primes))
    print(primes[0])