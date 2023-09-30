from enum import Enum
from sys import stdin
from typing import Final, Literal

class Tile(Enum):
    EMPTY = 0
    APPLE = 1
    SNAKE = 2

Direction = tuple[Literal[-1, 0, 1], Literal[-1, 0, 1]]

N: Final[int] = int(stdin.readline())
world: list[list[Tile]] = [[Tile.EMPTY for _ in range(N)] for _ in range(N)]
world[0][0] = Tile.SNAKE
K: Final[int] = int(stdin.readline())

for _ in range(K):
    y, x = map(int, stdin.readline().split())
    world[y - 1][x - 1] = Tile.APPLE

L: Final[int] = int(stdin.readline())
curves: list[tuple[int, bool]] = []                 # True면 오른쪽, False면 왼쪽
for _ in range(L):
    t, c = stdin.readline().split()
    curves.append((int(t), True if c == "D" else False))

print("Curves:")
for t, c in curves:
    print(f"{t} => {'Right' if c else 'Left'}")
# curves.sort(key=lambda x: x[0])                   # 정렬할 필요 없음

snake_len: int = 1
snake: list[list[int]] = [[0, 0]]                                       # y, x
time: int = 0
dir_index: int = 0
DIRECTIONS: tuple[Direction, Direction, Direction, Direction] = ((0, 1), (1, 0), (0, -1), (-1, 0))     # y, x

def forward() -> bool:
    """뱀을 현재 방향대로 전진시킨다.

    Returns:
        bool: 전진에 성공하면 True, 벽에 부딪히면 False.
    """
    dir_y, dir_x = DIRECTIONS[dir_index]
    head_y, head_x = snake[0]
    new_y = head_y + dir_y
    new_x = head_x + dir_x
    if new_x < 0 or new_x >= N or new_y < 0 or new_y >= N:
        return False
    if world[new_y][new_x] == Tile.SNAKE:
        return False
    
    snake.insert(0, [new_y, new_x])
    return True

def print_world():
    DIRECTION_CHAR: tuple[str, str, str, str] = ("▶️ ", "🔽 ", "◀️ ", "🔼 ")
    print(f"World : time = {time}, len = {snake_len}, head = {snake[0]}, dir = {DIRECTIONS[dir_index]}")
    for y, line in enumerate(world):
        for x, tile in enumerate(line):
            match tile:
                case Tile.APPLE:
                    print("🍎", end="")
                case Tile.EMPTY:
                    print("⬜", end="")
                case Tile.SNAKE:
                    if snake[0][0] == y and snake[0][1] == x:
                        print(DIRECTION_CHAR[dir_index], end="")
                    else:
                        print("🟩", end="")
        print()
    print("=" * 10)

print_world()
while snake_len > 0:
    time += 1
    
    # 벽에 부딪혔는가?
    is_dead = forward()
    if not is_dead:
        break
    
    # 현재 머리 위치의 타일 계산
    y, x = snake[0]
    
    if world[y][x] == Tile.APPLE:
        snake_len += 1
        world[y][x] = Tile.SNAKE
    else:
        tail_y, tail_x = snake.pop()
        world[tail_y][tail_x] = Tile.EMPTY
        world[y][x] = Tile.SNAKE
    
    print_world()
    
    if len(curves) > 0 and time == curves[0][0]:
        _, is_right = curves.pop(0)
        if is_right:
            dir_index = (dir_index + 1) % 4
        else:
            dir_index = (dir_index - 1) % 4
print(time)
