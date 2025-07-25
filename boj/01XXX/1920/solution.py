# Migrated from ./boj/boj1920.py by boj_validator
from sys import stdin
from typing import Final

N: Final[int] = int(stdin.readline())
arrN: list[int] = sorted(map(int, stdin.readline().split()))
M: Final[int] = int(stdin.readline())
arrM: list[int] = list(map(int, stdin.readline().split()))

def binarySearch(number: int):
    left: int = 0
    right: int = N - 1
    
    while left <= right:
        mid: int = (left + right) // 2
        
        if arrN[mid] > number:
            right = mid - 1
        elif arrN[mid] < number:
            left = mid + 1
        else:
            print(1)
            return
    print(0)

for i in range(M):
    binarySearch(arrM[i])
