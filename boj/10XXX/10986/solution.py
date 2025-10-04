from sys import stdin
input = map(int, stdin.buffer.read().split()) # 입력 스트리밍
N = next(input)
M = next(input)
freq_r = [0] * M
freq_r[0] = 1 # S_0은 항상 0이다. / S_0을 포함해 두어야, 시작점이 1인 모든 구간을 제대로 정답에 포함할 수 있다.

S = 0
for i in range(N):
    S = (S + next(input) % M) % M
    freq_r[S] += 1

answer = 0
for r in freq_r:
    answer += r * (r - 1) // 2
print(answer)
