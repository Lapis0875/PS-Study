input = open(0).readline
sudoku = [[0 for _ in range(9)] for _ in range(9)]
rows = [[False for _ in range(10)] for _ in range(10)]
cols = [[False for _ in range(10)] for _ in range(10)]
grids = [[False for _ in range(10)] for _ in range(10)]

blanks = [] # [r, c, v]
answer_found = False

def get_grid_idx(r, c):
    return (r - r % 3) + c // 3

def init():
    for target_arr in (rows, cols, grids):
        for i in range(10):
            for j in range(10):
                target_arr[i][j] = False
    
def check_sudoku_valid():
    for r in range(9):
        for c, v in enumerate(map(int, input().strip())):
            sudoku[r][c] = v
            if v == 0:
                blanks.append((r, c))
            else:
                grids_idx = get_grid_idx(r, c)
                if rows[r][v] or cols[c][v] or grids[grids_idx][v]:
                    # 만약 잘못된 입력의 경우 더 이상 처리하지 않고 오답처리 후 다음 케이스를 처리한다.
                    return False

                rows[r][v] = True
                cols[c][v] = True
                grids[grids_idx][v] = True
    
    return True


def dfs(depth):
    # print(f"dfs({depth})")
    # print(blanks)
    if depth == 5:
        global answer_found
        print("\n".join("".join(map(str, sudoku[r])) for r in range(9)) + "\n")
        answer_found = True
        return
    
    cur_r, cur_c = blanks[depth]
    for v in range(1, 10):
        # print(f"dfs({depth}) >>> trying {v}")
        if not rows[cur_r][v] and not cols[cur_c][v] and not grids[get_grid_idx(cur_r, cur_c)][v]:
            sudoku[cur_r][cur_c] = v
            dfs(depth + 1)
    sudoku[cur_r][cur_c] = 0

for i in range(int(input())):
    init()
    if not check_sudoku_valid():
        print("Could not complete this grid.\n")
        continue
    
    dfs(0)
    if not answer_found:
        print("Could not complete this grid.\n")
    