input = open(0).readline

sudoku = [[0 for _ in range(9)] for _ in range(9)]
rows = [[False for _ in range(10)] for _ in range(9)]
cols = [[False for _ in range(10)] for _ in range(9)]
grids = [[False for _ in range(10)] for _ in range(9)]
blanks = []     # [(r, c)] 형태로 빈칸의 좌표를 저장한다.
values = []     # 백트래킹을 진행하면서 답을 채울 배열
answer = []     # 사전순으로 가장 빠른 답을 저장할 배열

for r in range(9):
    for c, v in enumerate(map(int, input().strip())):
        sudoku[r][c] = v
        if v == 0:
            blanks.append((r, c))
        else:
            grids_idx = (r // 3) * 3 + (c // 3)
            rows[r][v] = True
            cols[c][v] = True
            grids[grids_idx][v] = True

blank_count = len(blanks)
values.extend(0 for _ in range(blank_count))
answer.extend(10 for _ in range(blank_count))

def update_answer():
    """정답 배열(answer)을 현재 분기에서 찾은 답(values)으로 갱신합니다."""
    for i in range(blank_count):
        if values[i] < answer[i]:
            for j in range(blank_count):
                answer[j] = values[j]
            return

def backtracking(depth):
    if depth == blank_count:
        for i in range(blank_count):
            if values[i] < answer[i]:
                update_answer()
                return
    
    r, c = blanks[depth]
    grids_idx = (r // 3) * 3 + (c // 3)
    for v in range(1, 10):
        # 이전에 발견한 정답보다 사전순으로 뒤에 위치하는 분기는 탐색하지 않는다.
        if v > answer[depth]:
            break
        
        if not rows[r][v] and not cols[c][v] and not grids[grids_idx][v]:
            # 분기 변수 설정
            sudoku[r][c] = v
            rows[r][v] = True
            cols[c][v] = True
            grids[grids_idx][v] = True
            values[depth] = v
            # DFS (백트래킹)
            backtracking(depth + 1)
            # 분기 변수 초기화
            rows[r][v] = False
            cols[c][v] = False
            grids[grids_idx][v] = False
        values[depth] = 0

backtracking(0)

# 결과 출력하기
for i in range(blank_count):
    r, c = blanks[i]
    sudoku[r][c] = answer[i]

print("\n".join("".join(map(str, row)) for row in sudoku))