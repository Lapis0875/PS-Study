input = open(0).readline

N = int(input())
arr = sorted(map(int, input().split()))
X = int(input())

a = 0
b = 1
res = 0
while a < N - 1 and a < b:
    b = a + 1
    while b < N and arr[a] + arr[b] < X:
        b += 1
    
    if b < N and arr[a] + arr[b] == X:
        res += 1
    
    a += 1

print(res)
