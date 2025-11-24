from math import sqrt
input = open(0).readline

MAX_N = 1000001
is_prime = [True] * MAX_N
is_prime[0] = is_prime[1] = False

for i in range(2, int(sqrt(MAX_N)) + 1):
    if is_prime[i]:
        for j in range(i * i, MAX_N, i):
            is_prime[j] = False

primes = []
for i in range(MAX_N):
    if is_prime[i]:
        primes.append(i)

for _ in range(int(input())):
    N = int(input())
    cnt = 0
    for prime in primes:
        if prime * 2 > N:
            break
        print(prime, N - prime)
        if is_prime[N - prime]:
            cnt += 1
    print(cnt)