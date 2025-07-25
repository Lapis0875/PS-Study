from math import ceil, sqrt
input = open(0).readline
K = int(input())

primes = []
i = 2
while K > 1 and i <= ceil(sqrt(K)):
    if K % i == 0:
        primes.append(i)
        K //= i
    else:
        i += 1

if K > 1:
    print(len(primes) + 1)
    print(*primes, K)
else:
    print(len(primes))
    print(" ".join(map(str, primes)))
