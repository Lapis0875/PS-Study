from collections import deque
input = open(0).readline
N, B = map(int, input().split())
convert = ["" for _ in range(36)]
for i in range(10):
    convert[i] = str(i)
for i in range(10, 36):
    convert[i] = chr(i + 55) # i = 10 ... 26이므로, i + 55는 65(A)...81(Z)가 된다.

ans = deque()
while N > 0:
    ans.append(N % B)
    N //= B

while ans:
    print(convert[ans.pop()], end="")
print()