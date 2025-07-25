input = open(0).readline
N = int(input().strip())
A = list(map(int, input().strip().split()))
lis = [0 for _ in range(N)]
record = [0 for _ in range(N)]
lis[0] = A[0]
record[0] = 1

def binary_search(left, right, value):
    while left < right:
        mid = (left + right) // 2
        if lis[mid] < value:
            left = mid + 1
        else:
            right = mid
    return right

j = 0
for i in range(1, N):
    if A[i] > lis[j]: # 현재 LIS의 마지막 원소보다 이번 원소가 더 크다면
        j += 1
        lis[j] = A[i]
        record[i] = j + 1
    else:   # 그렇지 않다면, 이번 원소를 lis의 어디에 넣을지 이분탐색으로 결정한다.
        idx = binary_search(0, j, A[i])
        lis[idx] = A[i]
        record[i] = idx + 1

lis_result = [0 for _ in range(j + 1)]
idx = j + 1
i = N - 1
while idx > 0 and i >= 0:
    if record[i] == idx:
        lis_result[j + 1 - idx] = A[i]
        idx -= 1
    i -= 1
print(j + 1)
print(*lis_result[::-1])