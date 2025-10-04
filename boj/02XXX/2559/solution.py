input = open(0).readline
N, K = map(int, input().split())

arr = list(map(int, input().split()))
max_temp = cur_sum = sum(arr[:K])
for i in range(1, N - K + 1):
    cur_sum -= arr[i - 1]
    cur_sum += arr[i + K - 1]
    max_temp = max(max_temp, cur_sum)

print(max_temp)