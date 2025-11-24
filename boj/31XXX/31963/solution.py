from math import log2, ceil
input = open(0).readline
N = int(input())
A = list(map(int, input().split()))

cnt = 0
prev = 0
for i in range(1, N):
    cur_log = log2(A[i - 1] / A[i]) # 앞의 수와의 크기 차이를 log2로 계산 / 앞의 수보다 커지려면 2를 몇 번 곱해야 하는지의 값이 된다.
    res = ceil(cur_log) + prev # 앞의 수도 이전 연산을 통해 저장된 값 보다 커졌으니, 해당 크기 차이를 반영하기 위해 이전 연산 결과 prev를 더한다.
    if res > 0: # res > 0일때는 2를 양수 번 곱한 것.
        cnt += res
        prev = res # A[i]가 커졌으니 커진만큼 prev를 반영
    else: # A[i]에 2를 곱하지 않은 경우
        prev = 0 # A[i]값과 동일하니 굳이 반영할 prev값은 없다

print(cnt)
