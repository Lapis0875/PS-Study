input = open(0).readline

sudoku = [[0 for _ in range(9)] for _ in range(9)]
rows = [[False for _ in range(10)] for _ in range(9)]
cols = [[False for _ in range(10)] for _ in range(9)]
grids = [[False for _ in range(10)] for _ in range(9)]
blanks = [None] * 5     # [(r, c)] 형태로 빈칸의 좌표를 저장한다.

def handle_input():
    """입력값을 읽어 sudoku, rows, cols, grids, blanks를 초기화합니다."""
    data = [input().strip() for _ in range(9)] # 반드시 이번 케이스의 입력을 모두 읽어야 한다.

    # 스도쿠 입력 및 상태변수 갱신
    blank_cnt = 0
    for r in range(9):
        for c, v in enumerate(map(int, data[r])):
            sudoku[r][c] = v
            if v == 0:
                blanks[blank_cnt] = (r, c)
                blank_cnt += 1
            else:
                grids_idx = (r // 3) * 3 + (c // 3)
                if rows[r][v] or cols[c][v] or grids[grids_idx][v]:
                    return False  # 잘못된 입력 처리
                rows[r][v] = True
                cols[c][v] = True
                grids[grids_idx][v] = True

    return True

def backtracking(depth):
    global found
    if found:   # 이미 정답을 찾았으므로 더 이상 탐색하지 않습니다.
        return

    if depth == 5:
        found = True
        return
    
    r, c = blanks[depth]
    grids_idx = (r // 3) * 3 + (c // 3)
    for v in range(1, 10):
        if not found and not rows[r][v] and not cols[c][v] and not grids[grids_idx][v]:
            # 분기 변수 설정
            rows[r][v] = True
            cols[c][v] = True
            grids[grids_idx][v] = True
            sudoku[r][c] = v
            # DFS (백트래킹)
            backtracking(depth + 1)
            if found:
                return
            # 분기 변수 초기화
            rows[r][v] = False
            cols[c][v] = False
            grids[grids_idx][v] = False
    sudoku[r][c] = 0

for _ in range(int(input())):
    # 상태 변수 초기화
    found = False
    for idx in range(9):
        for number in range(1, 10):
            rows[idx][number] = False
            cols[idx][number] = False
            grids[idx][number] = False
    
    # 초기 입력 검증
    is_correct = handle_input()
    if not is_correct:
        print("Could not complete this grid.\n")
        continue

    # 백트래킹으로 스도쿠 풀기
    backtracking(0)

    # 정답에 따라 결과 처리하기
    if found:
        # 결과 출력하기
        print("\n".join("".join(map(str, row)) for row in sudoku))
    else:
        print("Could not complete this grid.")
    print()
