input = open(0).readline

N = int(input())
cnt = 0
i = 1
while i * i <= N:
    i += 1
    cnt += 1
print(cnt)