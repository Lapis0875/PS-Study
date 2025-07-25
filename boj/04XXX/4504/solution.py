from sys import stdin
from typing import Final

N: Final[int] = int(stdin.readline())

while (x := int(stdin.readline())) != 0:
    print(f"{x} is {'NOT ' if x % 3 else ''}a multiple of {N}.")
