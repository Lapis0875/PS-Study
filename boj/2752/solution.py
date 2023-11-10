from sys import stdin

numbers: list[int] = sorted(map(int, stdin.readline().split()))
print(" ".join(map(str, numbers)))