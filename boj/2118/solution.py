input = open(0).readline
N = int(input())
distance = [int(input()) for _ in range(N)]
total_distance = sum(distance)
prefix_sum = [0 for _ in range(2 * N + 1)]    # 원형 구조를 고려해 2배 크기로 설정.
for i in range(2 * N):
    prefix_sum[i + 1] = prefix_sum[i] + distance[i % N]

max_distance = 0
right = 1
for left in range(2 * N):
    while right < 2 * N + 1 and (left_distance := prefix_sum[right] - prefix_sum[left]) <= total_distance - left_distance:
        max_distance = max(max_distance, left_distance)
        right += 1

print(max_distance)  # 최대거리 출력
