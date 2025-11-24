input = open(0).readline
A, B = map(int, input().split())
if B > A:
    A, B = B, A

def gcd(a, b):
    while b > 0:
        a, b = b, a % b
    return a

print(A * B // gcd(A, B))
