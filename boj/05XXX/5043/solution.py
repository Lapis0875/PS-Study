N, B = map(int, input().split())
print("yes" if N <= (1 << (B + 1)) - 1 else "no")