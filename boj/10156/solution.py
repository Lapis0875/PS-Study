# Migrated from ./boj/boj10156.py by boj_validator
(a:=[int(c) for c in input().split()], print(0 if (p:=a[0]*a[1])<=a[2] else p-a[2]))