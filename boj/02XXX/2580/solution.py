input = open(0).readline

rows = [[False for _ in range(10)] for _ in range(9)]
cols = [[False for _ in range(10)] for _ in range(9)]
grids = [[False for _ in range(10)] for _ in range(9)]

def get_grid_idx(r, c):
    return r // 3 * 3 + c // 3

sudoku = [[0 for _ in range(9)] for _ in range(9)]
blanks = []

for r in range(9):
    for c, t in enumerate(map(int, input().split())):
        if t == 0:
            blanks.append((r, c))
        else:
            sudoku[r][c] = t
            rows[r][t] = True
            cols[c][t] = True
            grids[get_grid_idx(r, c)][t] = True

def print_sudoku():
    for r in range(9):
        print(" ".join(map(str, sudoku[r])))

def backtracking(depth):
    if depth == len(blanks):
        print_sudoku()
        return True
    
    r, c = blanks[depth]
    g = get_grid_idx(r, c)
    for i in range(1, 10):
        if rows[r][i] or cols[c][i] or grids[g][i]:
            continue
        # set blank to i
        sudoku[r][c] = i
        rows[r][i] = True
        cols[c][i] = True
        grids[g][i] = True

        # backtracking
        if backtracking(depth + 1):
            return

        # undo
        rows[r][i] = False
        cols[c][i] = False
        grids[g][i] = False

    sudoku[r][c] = 0
    return False

backtracking(0)