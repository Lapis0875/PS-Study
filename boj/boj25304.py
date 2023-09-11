from sys import stdin


X: int = int(stdin.readline())
N: int = int(stdin.readline())
total: int = 0

for _ in range(N):
    a, b = map(int, stdin.readline().split())
    total += a * b

print("Yes" if total == X else "No")
    