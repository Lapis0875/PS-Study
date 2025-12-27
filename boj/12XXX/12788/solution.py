input = open(0).readline
N = int(input())
M, K = map(int, input().split())
pens = sorted(map(int, input().split()), reverse=True)

req = M * K
cnt = 0
while req > 0 and cnt < N:
    req -= pens[cnt]
    cnt += 1
if req > 0:
    print("STRESS")
else:
    print(cnt)