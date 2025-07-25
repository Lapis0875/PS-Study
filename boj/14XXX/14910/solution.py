from sys import stdin
from typing import Iterable

numbers: Iterable[int] = map(int, stdin.readline().split())
prev: int = next(numbers)
for cur in numbers:
    if prev > cur:
        print("Bad")
        break
    prev = cur
else:
    print("Good")