from sys import stdin
from typing import Literal

T: int = int(stdin.readline())

def is_palindrome(word: str, is_pseudo_check: bool = False) -> Literal[0, 1, 2]:
    left: int = 0
    right: int = len(word) - 1
    answer: Literal[0, 1, 2] = 0
    while left <= right:
        if word[left] == word[right]:                           # 회문 
            left += 1
            right -= 1
        elif answer == 0 and not is_pseudo_check:     # 유사 회문 (처음 발견한 경우에만)
            left_part: bool = is_palindrome(word[left + 1:right+1], True) == 0 # left + 1 ~ right 까지가 회문인지 검사한다.
            right_part: bool = is_palindrome(word[left:right], True) == 0 # left ~ right - 1 까지가 회문인지 검사한다.
            return 1 if any((left_part, right_part)) else 2
        else:                                                   # 회문이 아니다
            return 2
    return answer

for _ in range(T):
    word: str = stdin.readline().rstrip()
    print(is_palindrome(word))
