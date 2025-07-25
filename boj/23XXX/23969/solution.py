from sys import stdin
N, K = map(int, stdin.readline().split())
A = list(map(int, stdin.readline().split()))

cnt = 0
for last in range(N-1, 0, -1):
    for i in range(last):
        if A[i] > A[i+1]:
            A[i], A[i+1] = A[i+1], A[i]
            cnt += 1
        if cnt == K:
            break
    if cnt == K:
        break

if cnt < K:
    print(-1)
else:
    print(" ".join(map(str, A)))

