# Migrated from ./boj/boj1463.py by boj_validator
from sys import stdin
from typing import Final

X: int = int(stdin.readline())
MAX_OP: Final[int] = X + 1  # X를 1로 만드는 연산의 최대 횟수는 1씩 X번 빼는 것이므로, X + 1이 최대 횟수보다 큰 가장 작은 정수이다.
dp: list[int] = [MAX_OP] * X    # 0 ~ X - 1까지
dp.append(0)                    # X번 인덱스 추가

while X > 1:
    inc: int = dp[X] + 1
    if X % 3 == 0:
        i: int = X // 3
        if inc < dp[i]:
            dp[i] = inc
    
    if X % 2 == 0:
        i: int = X // 2
        if inc < dp[i]:
            dp[i] = inc
    
    if X > 1:
        i: int = X - 1
        if inc < dp[i]:
            dp[i] = inc

    X -= 1

print(dp[1])