from sys import stdin
from typing import Final, Literal

type WB = Literal[0, 1]
type MediaPart = list[list[WB]]

N: Final[int] = int(stdin.readline())
base = N
exp = 0
while base > 1:
    base >> 1
    exp += 1

media: MediaPart = []
loc: tuple[tuple[int, int]] = ((0, 0), (0, 1), (1, 0), (1, 1))      # idx -> (x, y)

for _ in range(N):
    media.append(list(map(int, stdin.readline().strip())))

def quadtree(idx: int, cell: int, start_x: int = 0, start_y: int = 0) -> str:
    """Quad Tree 압축 알고리즘을 구현한다.

    Args:
        idx (int): 현재 셀의 번호. [0 1 / 2 3] 구성이다.
        cell (int): 현재 셀의 크기.

    Returns:
        str: 현재 셀의 압축 결과.
    """
    if cell == 1:
        x, y = loc[idx]
        return str(media[y][x])
    
    recurse: bool = False
    parts: list[str] = ["", "", "", ""]
    half: int = cell // 2
    for idx in range(4):
        x, y = loc[idx]
        base = media[y][x]
        for y in range(start_x + y * half, start_x + y * half + y * half):
            if recurse:
                break
            for x in range(start_x + x * half, start_x + x * half + x * half):
                if recurse:
                    break
                if media[y][x] != base:
                    recurse = True
        if recurse:
            parts[idx] = "".join([
                quadtree(0, half, start_x, start_y),
                quadtree(1, half, start_x + half, start_y),
                quadtree(2, half, start_x, start_y + half),
                quadtree(3, half, start_x + half, start_y + half),
            ])
        else:
            parts[idx] = str(base)
    return f"({parts[0]}{parts[1]}{parts[2]}{parts[3]})"

print(quadtree(0, exp))