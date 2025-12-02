input = open(0).readline
N, C = map(int, input().split())
houses = sorted(int(input()) for _ in range(N))

# 매개변수 탐색
# 결정 문제: 인접한 두 공유기 사이의 최소 거리 K에 대해 C개 이상의 공유기를 설치할 수 있는가?
# TTTT...TFFFF
left = 1
right = houses[N - 1] - houses[0] + 1 # right값은 매개변수 탐색 과정에서 항상 도달할 수 없는 값에 해당함. 마지막집-첫집 값으로 사용할 경우 해당 값이 탐색 범위에서 배제됨.
while left + 1 < right: # left < right 조건에서는 left = mid인 경우 무한 루프가 일어난다. left + 1 < right일때는 항상 left < mid < right가 성립하므로 무한루프가 일어나지 않는다.
    mid = (left + right) // 2 # 공유기 사이 최소 간격

    # 결정 문제 풀이
    cnt = 1 # 첫 번째 집에 공유기 설치
    last_pos = houses[0]
    for i in range(1, N):
        if houses[i] - last_pos >= mid:
            cnt += 1
            last_pos = houses[i]
    if cnt >= C: # 결정 문제 T
        left = mid
    else: # 결정 문제 F
        right = mid
        
print(left)