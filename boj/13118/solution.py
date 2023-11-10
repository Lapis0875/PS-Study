from sys import stdin

people: list[int] = list(map(int, stdin.readline().split()))
x, _, _ = map(int, stdin.readline().split())

crashed: bool = False
for i, p in enumerate(people, 1):
    if p == x:
        print(i)
        crashed = True

if not crashed:
    print(0)