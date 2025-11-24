input = open(0).readline
N = int(input())

primes_acc = [0, ]
sieve = [True] * 4_000_001
sieve[0] = sieve[1] = False

for i in range(2, 2_001): # sqrt(4_000_000) = 2000
    if sieve[i]:
        j = i * 2
        while j <= 4_000_000:
            sieve[j] = False
            j += i
for i in range(4_000_001):
    if sieve[i]:
        primes_acc.append(primes_acc[-1] + i)
primes_cnt = len(primes_acc)

cnt = 0
for start in range(primes_cnt):
    end = start + 1
    while end < primes_cnt:
        total = primes_acc[end] - primes_acc[start]
        if total > N:
            break
        elif total == N:
            cnt += 1
            break
        end += 1

print(cnt)