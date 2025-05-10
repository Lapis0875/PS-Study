# Migrated from ./boj/boj3009_counter.py by boj_validator
from collections import Counter

points: list[tuple[int, int]] = [tuple(map(int, input().split())) for _ in range(3)]

print(points)

xc: list[tuple[int, int]] = Counter(map(lambda t: t[0], points)).most_common()
yc: list[tuple[int, int]] = Counter(map(lambda t: t[1], points)).most_common()

print(xc)
print(yc)

print(xc[1][0], yc[1][0])