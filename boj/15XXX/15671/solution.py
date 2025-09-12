from collections import deque
input = open(0).readline

# 타일 상수
EMPTY = 0
WHITE = 1
BLACK = 2
TILE_STR = [".", "W", "B"]
DIRECTIONS = ((-1, -1), (-1, 0), (-1, 1), (0, -1), (0, 1), (1, -1), (1, 0), (1, 1))

board = [[EMPTY for _ in range(7)] for _ in range(7)]
queue = deque()

board[3][3] = board[4][4] = WHITE
board[3][4] = board[4][3] = BLACK

def print_answer():
    white = 0
    black = 0
    t = [""] * 6
    for r in range(1, 7):
        for c in range(1, 7):
            if board[r][c] == WHITE:
                white += 1
            elif board[r][c] == BLACK:
                black += 1
            t[c - 1] = TILE_STR[board[r][c]]
        print("".join(t))
    if white > black:
        print("White")
    else: # 비기는 입력은 주어지지 않는다.
        print("Black")

def is_inside(r, c):
    return 1 <= r <= 6 and 1 <= c <= 6

def check_board(r, c, stone):
    for dr, dc in DIRECTIONS:
        nr = r + dr
        nc = c + dc
        queue.clear()

        while is_inside(nr, nc):
            if board[nr][nc] == EMPTY:
                break
            elif board[nr][nc] == stone:
                while queue:
                    nr, nc = queue.popleft()
                    board[nr][nc] = stone
                break
            else:
                queue.append((nr, nc))
            nr += dr
            nc += dc

for i in range(1, int(input()) + 1):
    r, c = map(int, input().split())
    cur_turn = BLACK if i & 1 else WHITE
    board[r][c] = cur_turn
    check_board(r, c, cur_turn)

print_answer()
