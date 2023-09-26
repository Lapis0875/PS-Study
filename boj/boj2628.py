from sys import stdin

width, height = map(int, stdin.readline().split())
N: int = int(stdin.readline())

vertical: list[int] = [0, width]
horizontal: list[int] = [0, height]

for _ in range(N):
    direction, pos = map(int, stdin.readline().split())
    if direction:
        vertical.append(pos)
    else:
        horizontal.append(pos)

vertical.sort()
horizontal.sort()

max_area: int = 0

for v in range(len(vertical) - 1):
    for h in range(len(horizontal) - 1):
        max_area = max((vertical[v + 1] - vertical[v]) * (horizontal[h + 1] - horizontal[h]), max_area)

print(max_area)
