from sys import stdin
from typing import cast, Literal

PaperType = Literal[-1, 0, 1]
Coordinate = tuple[int, int]    # (x, y)
Count = tuple[int, int, int]         # (-1, 0, 1)
N: int = int(stdin.readline())

paper: list[list[PaperType]] = [list(map(lambda x: cast(PaperType, int(x)), stdin.readline().split())) for _ in range(N)]


def print_paper(lu: Coordinate, size: int):
    x, y = lu
    for r in range(y, y + size):
        for c in range(x, x + size):
            print(paper[r][c], end=" ")
        print()

def parse_papers(lu: Coordinate, size: int) -> Count:
    # print(f">>> parse_papers({lu}, {size})")
    # print_paper(lu, size)
    x, y = lu
    pt: PaperType = paper[y][x]
    
    if size == 1:
        match pt:
            case -1:
                return (1, 0, 0)
            case 0:
                return (0, 1, 0)
            case 1:
                return (0, 0, 1)
    
    is_single: bool = True
    for i in range(y, y + size):
        for j in range(x, x + size):
            if paper[i][j] != pt:
                is_single = False
                break                       # size x size가 한개의 색종이가 아니다! 쪼개야 함.
        if not is_single:
            break                           # 이미 재귀하기로 결정했다면 루프 바로 나가자.
    
    if is_single:                           # size x size가 한개의 색종이다!
        match pt:
            case -1:
                return (1, 0, 0)
            case 0:
                return (0, 1, 0)
            case 1:
                return (0, 0, 1)
    
    cnt: list[int] = [0, 0, 0]
    next_size: int = size // 3
    for i in range(3):
        for j in range(3):
            res = parse_papers((x + next_size * i, y + next_size * j), next_size)
            for idx, c in enumerate(res):
                cnt[idx] += c
    return cast(Count, tuple(cnt))
    
print(*parse_papers((0, 0), N), sep="\n")
