input = open(0).readline

N = int(input())
times = list(map(int, input().split()))
min_time = 100000
max_time = 1

for t in times:
    min_time = min(min_time, t)
    max_time = max(max_time, t)

left = min_time
right = max_time

while left <= right:
    mid = (left + right) // 2
    required_time_sectors = 0
    for t in times:
        required_time_sectors += (t + mid - 1) // mid  # ceil(t / mid)
    if required_time_sectors < 2 * N: # N
        right = mid - 1
    else: # N
        left = mid + 1

print(left)
