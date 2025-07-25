from sys import stdin

N: int = int(stdin.readline())
pattern: str = ("* " * N).rstrip()

for row in range(1, N + 1):
    if row % 2:
        print(pattern)
    else:
        print(" " + pattern)