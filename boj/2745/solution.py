# Migrated from ./boj/boj2745.py by boj_validator
from sys import stdin

target, base = stdin.readline().split()
base = int(base)

decimal: int = 0
for digit in target[::-1]:
    decimal += int(digit) if digit.isdigit() else ord(digit) - 55
