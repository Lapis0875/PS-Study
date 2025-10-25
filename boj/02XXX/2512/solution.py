input = open(0).readline

N = int(input())
budgets = list(map(int, input().split()))
total_budget = int(input())

max_budget = 0
total = 0
for b in budgets:
    total += b
    max_budget = max(max_budget, b)

if total <= total_budget:
    print(max_budget)
else:
    left = 0                    # 기관별 예산 요구값의 최솟값조차 상한액보다 클 수 있다.
    right = 100000              # 어차피 상한액이 예산 최대값보다 클 필요는 없으니까
    while (left <= right):
        mid = (left + right) // 2

        # mid를 상한액으로 정하고 문제를 풀 때 답 구하기
        total = 0
        for i in range(N):
            total += min(budgets[i], mid)
        
        if total <= total_budget: # 답이 Y: 정답은 [mid, right] 구간에 존재
            left = mid + 1
        else: # 답이 N: 정답은 [left, mid-1] 구간에 존재
            right = mid - 1
    print(right)
