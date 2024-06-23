from sys import stdin
from typing import Final

N: Final[int] = int(stdin.readline())
X: str = "".join(stdin.readline().split())
Y: str = "".join(stdin.readline().split())

x: int = int(X)
y: int = int(Y)
print(x if x < y else y)