input = open(0).readline
N, M = map(int, input().split())

A = [[] for _ in range(N)]
B = [[] for _ in range(N)]
for r in range(N):
    A[r].extend(input().rstrip())
for r in range(N):
    B[r].extend(input().rstrip())

res = True
for r in range(N):
    for i in range(M):
        if B[r][2 * i] != A[r][i] or B[r][2 * i + 1] != A[r][i]:
            res = False
            break
    if not res: # 반복문이 중단된 경우
        break

print("Eyfa" if res else "Not Eyfa")