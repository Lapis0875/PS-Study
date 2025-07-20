input = open(0).readline
N = int(input())
# 체스판을 45도 회전시켜서 룩을 배치하는 문제로 바꾼다.
rotated_length = 2 * N - 1
board = [[-1] * rotated_length for _ in range(rotated_length)]  # -1은 실제 체스판에는 존재하지 않는 칸이므로 계산에 사용해선 안된다.
for row in range(N):
    for col, tile in enumerate(map(int, input().split())):
        rotated_r = row + col
        rotated_c = N - 1 - row + col
        board[rotated_r][rotated_c] = tile

bishops = [[None for _ in range(rotated_length)] for _ in range(2)] # tuple[int, int]: bishop's position (r, c)
columns = [[True for _ in range(rotated_length)] for _ in range(2)] # 배치 가능한 열이면 True, 그렇지 않다면 False.
    
# 룩은 각 행/열에 한개씩만 존재할 수 있다.
# 최적화 팁: 비숍의 특징을 고려해보면, 흑칸 비숍과 백칸 비숍은 원래 서로 간섭하지 못한다. 따라서, 흑칸과 백칸을 나누어 푼 후 답을 더해도 된다!
max_bishops = [0, 0]
def backtracking(row, count, is_black):
    # print(f"backtracking({row}, {count})")
    # print("\n".join(map(lambda b: f"- {b}", bishops)))
    # print()

    if row >= rotated_length:
        # print("[ End of backtracking ]")
        max_bishops[is_black] = max(max_bishops[is_black], count)
        return

    for j in range(rotated_length):
        if board[row][j] == 1 and columns[is_black][j]:
            columns[is_black][j] = False
            bishops[is_black][count] = (row, j)
            backtracking(row + 2, count + 1, is_black)
            columns[is_black][j] = True
            bishops[is_black][count] = None
    backtracking(row + 2, count, is_black)
    # Q. 만약 for문 안에서 가능한 분기를 찾지 못하면, backtracking이 다음 행으로 넘어가지 못하고 종료된다.

# 홀수 행과 짝수 행을 나눠서 DFS
backtracking(0, 0, 0)
backtracking(1, 0, 1)
print(sum(max_bishops))