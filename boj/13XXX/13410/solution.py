# Migrated from ./boj/boj13410.py by boj_validator
N, K = map(int, input().split())

def reverseGuGu(x: int) -> int:
    reverse: list[int] = []
    while x > 0:
        reverse.append(x % 10)
        x //=10
    r: int = 0
    for i, base in zip(reverse, range(len(reverse) - 1, -1, -1)):
        r += i * (10 ** base)
    return r

maximum: int = 0
for i in range(1, K + 1):
    x: int = reverseGuGu(N * i)
    if x > maximum:
        maximum = x
print(maximum)