from decimal import Decimal, ROUND_HALF_UP, getcontext
getcontext().rounding = ROUND_HALF_UP

input = open(0).readline
N, K = map(int, input().split())
scores = sorted(Decimal(input().rstrip()) for _ in range(N))

trimmed_avg = sum(scores[K:N-K]) / (N - 2 * K)
print(f"{round(trimmed_avg, 2):.2f}")

adjusted_total = sum(scores[K:N-K]) + K * scores[K] + K * scores[N - K - 1]
adjusted_avg = adjusted_total / N
print(f"{round(adjusted_avg, 2):.2f}")