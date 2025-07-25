from sys import stdin

A, B = map(int, stdin.readline().split())
chicken: int = int(stdin.readline())

if (s := A + B) >= 2 * chicken:
    print(s - 2 * chicken)
else:
    print(s)