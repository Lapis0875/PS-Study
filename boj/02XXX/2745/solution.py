input = open(0).readline
N, B = input().split()
B = int(B)
A_ord = 65
ord_map = {chr(A_ord + k): 10 + k for k in range(26)}
ord_map.update({str(i): i for i in range(10)})

ans = 0
base = 1
for i in range(len(N) - 1, -1, -1):
    ans += ord_map[N[i]] * base
    base *= B

print(ans)
