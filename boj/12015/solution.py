input = open(0).readline
N = int(input().strip())
A = list(map(int, input().strip().split()))
lis = [0 for _ in range(N)]
lis[0] = A[0]

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
    else:   # 그렇지 않다면, 이번 원소를 lis의 어디에 넣을지 이분탐색으로 결정한다.
        idx = binary_search(0, j, A[i])
        lis[idx] = A[i]


print(j + 1)