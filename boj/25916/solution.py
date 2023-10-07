from sys import stdin

N, M = map(int, stdin.readline().split())

A: list[int] = list(map(int, stdin.readline().split()))


"""
size = 8 -> (0, 7)
size = 7 -> (0, 6) , (1, 7)
size = 6 -> (0, 5) , (1, 6), (2, 7)
size = 5 -> (0, 4) , (1, 5), (2, 6), (3, 7)
"""
right: int = 0
answer: int = 0
total: int = 0
for left in range(N):
    while right < N and total + A[right] <= M:
        total += A[right]
        right += 1
    answer = max(answer, total)                 # 현재 왼쪽 인덱스에 대한 최대 구간합 저장
    total -= A[left]                            # 왼쪽 인덱스 이동

print(answer)
