input = open(0).readline
N, M = map(int, input().split())
S = {input().rstrip(): 1 for _ in range(N)}

cnt = 0
for _ in range(M):
    try:
        cnt += S[input().rstrip()]
    except KeyError:
        pass

print(cnt)
