input = open(0).readline
A, B = map(int, input().split())
if B > A:
    A, B = B, A

while B > 0:
    A, B = B, A % B
print("1" * A)