# Migrated from ./boj/boj1343.py by boj_validator
from sys import stdin

board: str = stdin.readline()[:-1]

covered: list[str] = []
count: int = 0

def cover(cnt: int) -> bool:
    """
    . 이전까지의 보드를 폴리오미노로 덮는다.
    
    Args:
        cnt (int): X의 개수.
    
    Returns:
        bool: X가 남았는지 여부.
    """
    while cnt >= 4:
        cnt -= 4      # AAAA로 덮는다.
        covered.append("AAAA")
    while cnt >= 2:
        cnt -= 2
        covered.append("BB")
    return cnt > 0

for tile in board:
    if tile == ".":
        left: bool = cover(count)
        if left:
            print(-1)
            break
        covered.append(".")
    else:
        count += 1
else:
    left: bool = cover(count)
    print("".join(covered) if left else -1)
