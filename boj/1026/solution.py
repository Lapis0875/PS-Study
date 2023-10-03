from sys import stdin

N: int = int(stdin.readline())

A: list[int] = list(map(int, stdin.readline().split()))
sorted_a: list[int] = sorted(A)
B: list[int] = list(map(int, stdin.readline().split()))
sorted_b: list[int] = sorted(B, reverse=True)

print(sum(a * b for a, b in zip(sorted_a, sorted_b)))
