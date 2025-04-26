from sys import stdin

# 에라토스테네스의 체를 사용해 1부터 10,000까지의 소수를 미리 계산한다.
sieve = [True for _ in range(10_001)]
sieve[1] = False

for i in range(2, 100):
    if sieve[i]:
        j = 2
        while i * j <= 10_000:
            sieve[i * j] = False
            j += 1

happy_cache = {}


def happy_number(n):
    """주어진 수가 '행복한 수'인지 확인한다.
    행복한 수는 각 자리 숫자의 제곱의 합을 구하는 연산을 반복해 1이 되는 수이다.

    Args:
        n (int): 행복한 수인지 확인할 자연수

    Returns:
        bool: 행복한 수인지 여부
    """
    if n in happy_cache:
        return happy_cache[n]
    
    r = n
    trace = set()
    while r not in trace:
        trace.add(r)
        
        sum = 0
        while r > 0:
            sum += (r % 10) ** 2
            r //= 10
        if sum == 1:
            for t in trace:
                happy_cache[t] = True
            return True
        r = sum
    return False


P = int(stdin.readline().strip())
for _ in range(P):
    idx, M = map(int, stdin.readline().strip().split())
    # M이 소수인지 확인하고. 행복한 수인지 확인한 뒤 둘 다 참이라면 'YES', 그렇지 않다면 'NO'를 출력한다.
    print(f"{idx} {M} {'YES' if sieve[M] and happy_number(M) else 'NO'}")
