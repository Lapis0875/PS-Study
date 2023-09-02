from sys import stdin

N: int = int(stdin.readline())
A: list[int] = list(map(int, stdin.readline().split()))
if N > 1:
    diff: int = A[1] - A[0]
    for i in range(2, N):
        if A[i] - A[i - 1] != diff:
            print("NO")
            exit(0)
    print("YES")
else:
    diff: int = 0
    print("YES")
print(" ".join(map(lambda x: str(2 * x), A)))
print(" ".join(map(lambda x: str(-x), A)))