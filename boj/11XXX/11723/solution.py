# Migrated from ./boj/boj11723.py by boj_validator
from sys import stdin
from typing import Final

M: Final[int] = int(stdin.readline())

S: int = 0

def add(x: int):
    """S에 x를 추가한다. S에 x가 이미 있는 경우에는 연산을 무시한다.

    Args:
        x (int): (1 ≤ x ≤ 20)의 정수
    """
    global S
    S |= 1 << x

def remove(x: int):
    """S에서 x를 제거한다. S에 x가 이미 있는 경우에는 연산을 무시한다.

    Args:
        x (int): (1 ≤ x ≤ 20)의 정수
    """
    global S
    S &= ~(1 << x)

def check(x: int):
    """S에 x가 있으면 1을, 없으면 0을 출력한다.

    Args:
        x (int): (1 ≤ x ≤ 20)의 정수
    """
    print(1 if S & (1 << x) != 0 else 0)

def toggle(x: int):
    """S에 x가 있으면 x를 제거하고, 없으면 x를 추가한다. (1 ≤ x ≤ 20)

    Args:
        x (int): (1 ≤ x ≤ 20)의 정수
    """
    global S
    S ^= 1 << x

def all():
    """S를 {1, 2, ..., 20} 으로 바꾼다."""
    global S
    S = (1 << 21) - 1 # 1~20번째 자리 모두 1인 비트

def empty():
    """S를 공집합으로 바꾼다."""
    global S
    S = 0

local_vars = locals()

for _ in range(M):
    query: str = stdin.readline()[:-1]
    if " " in query:
        cmd, x = query.split()
        local_vars[cmd](int(x))
    else:
        local_vars[query]()
    # print(f">>> Query<' {query} '> , S : {S:b}")
