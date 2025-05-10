# Migrated from ./boj/boj1049.py by boj_validator
from sys import stdin

N, M = map(int, stdin.readline().split())
    
# 두 변수 모두 가격의 최대치인 1000보다 큰 값으로 설정한다.
cheapest_package: int = 1001
cheapest_single: int = 1001

for _ in range(M):
    p, s = map(int, stdin.readline().split())
    if p < cheapest_package:
        cheapest_package = p
    if s < cheapest_single:
        cheapest_single = s

# 1. 정확히 수량을 N개에 맞춰 혼합 구매
cost_exact: int = 0
n: int = N
while n > 0:
    if n >= 6 and n % 6 == 0:
        cost_exact += cheapest_package * (n // 6)
        break
    else:
        cost_exact += cheapest_single
        n -= 1

# 2. 전부 패키지로 구매
cost_package: int = (N // 6) * cheapest_package
if N % 6:                           # 만약 6의 배수로 딱 나누어 떨어지지 않는다면,
    cost_package += cheapest_package   # 개수룰 초과해서 패키지로 구매한다.

# 3. 전부 단품으로 구매
cost_single: int = N * cheapest_single

print(min(cost_exact, cost_package, cost_single))
