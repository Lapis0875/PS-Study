# Migrated from ./boj/boj25501.py by boj_validator
from sys import stdin
from typing import Literal

def recursion(s, l, r) -> tuple[Literal[1, 0], int]:        # Palindrome여부, 호출횟수
    if l >= r:                  # 끝까지 재귀. Palindrome이다.
        return 1, 1
    elif s[l] != s[r]:          # 재귀 중단. Palindrome이 아니다.
        return 0, 1
    else:                       # 계속 재귀한다.
        res, call = recursion(s, l+1, r-1)
        return res, call + 1

def isPalindrome(s) -> tuple[Literal[1, 0], int]:
    return recursion(s, 0, len(s)-1)

T: int = int(stdin.readline())
for _ in range(T):
    print(*isPalindrome(stdin.readline().strip()))
