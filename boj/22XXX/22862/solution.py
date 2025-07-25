from sys import stdin

N, K = map(int, stdin.readline().split())
S: list[int] = list(map(int, stdin.readline().split()))

if N == 1 and S[0] % 2:
    print(0)
else:
    # 변수
    left: int = 0
    right: int = 0          # 실제 right 위치는 매번 left가 증가할때마다 초기화된다.
    cnt: int = 0            # 현재 구간 내 홀수의 개수
    answer: int = 0         # 최종 정답
    while right < N:
        if cnt > K:             # 구간 내 홀수가 한도를 초과하면
            if S[left] % 2:         # 구간에서 제거한 수가 홀수인 경우 처리.
                cnt -= 1
            left += 1           # 왼쪽 포인터 한 칸 이동
        else:                   # 구간 내 홀수가 한도 이내라면
            if S[right] % 2:        # 구간에 새로 포함된 수가 홀수인 경우 처리.
                cnt += 1
            right += 1          # 오른쪽 포인터 한 칸 이동

        if cnt <= K and (l := right - left - cnt) > answer:
            # 1을 빼지 않는 이유 :
            # 현재 반복에서 left나 right의 값을 변경해도, 변경된 인덱스의 배열 원소를 검사하는 건 다음 번 반복에서 진행된다.
            # 구간 길이가 갱신되는건 right의 값이 증가하는 경우이므로,
            # 구간 길이를 계산하는 시점에 right는 이번 반복에서 다루는 구간보다 한 칸 더 오른쪽을 가리키고 있다.
            # 따라서, 우리가 흔히 범위 내의 길이를 계산하는 공식인 right - left + 1에서, 이미 (right + 1) - left를 계산한 것이므로 1을 더하지 않는다.
            answer = l

    print(answer)
