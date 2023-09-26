from sys import stdin

target, base = stdin.readline().split()
base = int(base)

decimal: int = 0
for digit in target[::-1]:
    decimal += int(digit) if digit.isdigit() else ord(digit) - 55
