input = open(0).readline
N, S = map(int, input().split())
arr = [0]
prefix_sum = [0]
for i, e in enumerate(map(int, input().split()), 1):
    arr.append(e)
    prefix_sum.append(prefix_sum[i - 1] + e)

total = 0
min_len = N + 1
l = 1
r = 1
while r <= N:
    total = prefix_sum[r] - prefix_sum[l - 1]
    length = r - l + 1
    if total >= S:
        if length < min_len:
            min_len = length
        l += 1
    else:
        r += 1

print(0 if min_len == N + 1 else min_len)