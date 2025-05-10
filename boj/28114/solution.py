# Migrated from ./boj/boj28114.py by boj_validator
from sys import stdin

enrolls: list[str] = []
names: list[tuple[int, str]] = []
for _ in range(3):
    solve, enrolled, family_name = stdin.readline().split()
    names.append((int(solve), family_name[0]))
    enrolls.append(enrolled[2:])

enrolls.sort()
print("".join(enrolls))

names.sort(key=lambda x: x[0], reverse=True)
print("".join([name[1] for name in names]))