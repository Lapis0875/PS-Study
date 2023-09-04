from sys import stdin

N, M = map(int, stdin.readline().split())

Trees: list[int] = []

left: int = 1
right: int = 0

for tree in map(int, stdin.readline().split()):
    Trees.append(tree)
    if tree > right:
        right = tree

mid: int = -1

while left <= right:
    mid = (left + right) // 2
    length: int = 0
    for tree in Trees:
        if tree > mid:
            length += tree - mid
    
    if length >= M:         # 너무 길게 잘랐으므로, 목재절단기의 높이를 높여야 한다.
        left = mid + 1
    else:                   # 너무 짧게 짤랐으므로, 목재절단기의 높이를 낮춰야 한다.
        right = mid - 1

print(right)
