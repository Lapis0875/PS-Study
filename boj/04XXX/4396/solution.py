input = open(0).readline
N = int(input().strip())
bombs = [[False for _ in range(N)] for _ in range(N)]
# 폭탄 좌표 처리
for y in range(N):
    line = input().strip()
    for x in range(N):
        if line[x] == "*":
            bombs[y][x] = True

def count_bombs(x, y):
    """자기 주위의 3x3 범위 안에 포함된 폭탄의 개수를 센다. (N이 10 이하이므로 매번 반복하면서 찾아도 시간 안에 풀 수 있다.)"""
    result = 0
    for dy in (-1, 0, 1):
        for dx in (-1, 0, 1):
            if 0 <= x + dx < N and 0 <= y + dy < N and bombs[y + dy][x + dx]:
                result += 1
    return result

# 칠해야 하는 범위 입력받기
board = []
failed = False
for y in range(N):
    line = list(input().strip())
    for x in range(N):
        if line[x] == "x":
            if bombs[y][x]:
                failed = True
            else:
                line[x] = count_bombs(x, y)
    board.append(line)

if failed:  # 만약 폭탄이 있는 위치가 열렸다면, 모든 폭탄이 *로 표시되어야 한다.
    for y in range(N):
        for x in range(N):
            if bombs[y][x]:
                board[y][x] = "*"

print("\n".join(map(lambda line: "".join(map(lambda c: str(c), line)), board)))
