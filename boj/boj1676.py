from sys import stdin
from typing import Final

N: Final[int] = int(stdin.readline())

# N! = 1 x 2 x ... x N
# => 곱해지는 수들 중, 곱해서 만들어진 10 의 개수를 세면 0 아닌 수 전까지의 뒤에서부터 0 개수와 같을 것이다!

two_fives: list[int] = [0, 0]
for i in range(1, N + 1):
    while i % 2 == 0:
        two_fives[0] += 1
        i //= 2
    while i % 5 == 0:
        two_fives[1] += 1
        i //= 5

print(min(two_fives))