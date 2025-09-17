from math import ceil, sqrt
input = open(0).readline
K, M = map(int, input().split())
SIZE = 10 ** K

# 1. 에라토스테네스의 체
sieve = [True for _ in range(SIZE)]
sieve[0] = sieve[1] = False
primes = []
for i in range(2, ceil(sqrt(SIZE))):
    if sieve[i]:
        for j in range(i * 2, SIZE, i):
            sieve[j] = False
for i in range(2, SIZE):
    if sieve[i]:
        primes.append(i)

# 2. 어떤 서로 다른 두 소수의 합과 곱으로 만들 수 있는 수를 범위 안에서 미리 다 만들어 두기
sum_of_primes = [False for _ in range(SIZE)]
mul_of_primes = [False for _ in range(SIZE)]
for i in range(len(primes)):
    for j in range(len(primes)):
        if i != j:
            value = primes[i] + primes[j]
            if value < SIZE:
                sum_of_primes[value] = True
        
        value = primes[i] * primes[j]
        if value < SIZE:
            mul_of_primes[value] = True
        elif primes[i] + primes[j] >= SIZE:
            break

# 2. 각 수에 대해 조건에 맞는지 검사하는 로직
def check(x):
    # 1) 서로 다른 두 개의 소수의 합으로 나타낼 수 있는 경우
    if not sum_of_primes[x]:
        return False
    
    # 2) M으로 나누어 떨어지지 않을때까지 나눈 수가 두 개의 소수의 곱인 경우, 이 때, 두 개의 소수가 같아도 된다.
    while x % M == 0:
        x //= M
    if not mul_of_primes[x]: # 두 개의 소수의 곱 = 합성수인 경우
        return False

    return True

# 3. 0 ~ 9 까지의 수를 K개 골라 만들 수 있는 모든 수 중 조건에 맞는 수를 추린다.
digits = [0, 0, 0, 0, 0]
def make_number():
    n = 0
    base = 1
    for i in range(K - 1, -1, -1):
        n += digits[i] * base
        base *= 10
    return n

visit = [False for _ in range(10)]
def backtrack(digit):
    res = 0
    if digit == K:
        return 1 if check(make_number()) else 0
    for i in range(10):
        if visit[i] or (digit == 0 and i == 0):
            continue
        digits[digit] = i
        visit[i] = True
        res += backtrack(digit + 1)
        visit[i] = False
    return res
     
print(backtrack(0))
