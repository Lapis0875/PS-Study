# Migrated from ./boj/boj3009.py by boj_validator
points: list[tuple[int, int]] = [tuple(map(int, input().split())) for _ in range(3)]

xc: dict[int, int] = {}
yc: dict[int, int] = {}

for point in points:
    x, y = point
    
    if x not in xc:
        xc[x] = 1
    else:
        xc[x] += 1
    
    if y not in yc:
        yc[y] = 1
    else:
        yc[y] += 1

minX, minY = points[0]

for point in points[1:]:
    x, y = point
    if xc[minX] > xc[x]:
        minX = x
    if yc[minY] > yc[y]:
        minY = y

print(minX, minY)