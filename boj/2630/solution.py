from sys import stdin

Coordinate = tuple[int, int]    # (x, y)
Count = tuple[int, int]         # (white, blue)
N: int = int(stdin.readline())

paper: list[list[bool]] = [list(map(lambda x: x == '1', stdin.readline().split())) for _ in range(N)]


def print_paper(lu: Coordinate, size: int):
    x, y = lu
    for r in range(y, y + size):
        for c in range(x, x + size):
            print("b" if paper[r][c] else "w", end=" ")
        print()

def parse_papers(lu: Coordinate, size: int) -> Count:
    # print(f">>> parse_papers({lu}, {size})")
    # print_paper(lu, size)
    x, y = lu
    
    if size == 1:
        return (0, 1) if paper[y][x] else (1, 0)
    
    color: bool = paper[y][x]
    is_single: bool = True
    for i in range(y, y + size):
        for j in range(x, x + size):
            if paper[i][j] != color:
                is_single = False
                break                       # size x size가 한개의 색종이가 아니다! 쪼개야 함.
        if not is_single:
            break                           # 이미 재귀하기로 결정했다면 루프 바로 나가자.
    
    if is_single:                           # size x size가 한개의 색종이다!
        return (0, 1) if color else (1, 0)
    
    white: int = 0
    blue: int = 0
    half_size: int = size // 2
    for i in range(2):
        for j in range(2):
            w, b = parse_papers((x + half_size * i, y + half_size * j), half_size)
            white += w
            blue += b
    return (white, blue)
    
print(*parse_papers((0, 0), N), sep="\n")
