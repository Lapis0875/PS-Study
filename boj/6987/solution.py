from bisect import insort_left
input = open(0).readline
N, K = map(int, input().split())
arr = list(map(int, input().split()))
buckets = [[] for _ in range(K)]

# 이분탐색으로 버킷 안에 넣을 인덱스 찾기 O(lg N)
# 최적화 문제로 생각하고 푼다: 버킷에 넣을 원소 e보다 작거나 같은 마지막 원소의 위치를 찾자.
for i in range(N):
    elem = arr[i]
    bucket = buckets[i % K]

    # insort_left(bucket, elem) # 내장 구현 사용하기
    l = 0
    r = len(bucket)
    # 결정 문제: elem이 bucket[m]보다 같거나 큰가?
    while l < r:
        m = (l + r) >> 1
        if bucket[m] < elem:    # N
            l = m + 1
        else:  # Y
            r = m
    bucket.insert(l, elem)

    # print(f"bucket[{i%K}] = {bucket}")

arr[0] = buckets[0][0]
for i in range(1, N):  # 정렬되어있는지 판단.
    arr[i] = buckets[i % K][i // K]
    if arr[i] < arr[i - 1]:
        print("No")
        break
else:
    print("Yes")
