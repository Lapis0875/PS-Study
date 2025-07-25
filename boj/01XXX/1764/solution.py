# Migrated from ./boj/boj1764.py by boj_validator
from sys import stdin

N, M = map(int, stdin.readline().split())

dontlisten: set[str] = {stdin.readline()[:-1] for _ in range(N)}
dontsee: set[str] = {stdin.readline()[:-1] for _ in range(N)}
dontknow: set[str] = dontlisten & dontsee

print(len(dontknow))
for person in sorted(dontknow):
    print(person)