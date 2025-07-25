from collections import deque
input = open(0).readline

N, M = map(int, input().split())
board = [0 for _ in range(101)]    # 방문 여부는 배열의 값이 0이 아닌지로 판단한다.
roads = [0 for _ in range(101)]
for _ in range(N + M):
    start, end = map(int, input().split())
    roads[start] = end

queue = deque([1])
while queue:
    current = queue.popleft()
    if current == 100:
        print(board[current])
        break
    for i in range(1, 7):       # 1~6까지 주사위를 굴려서 각 경우를 계산한다.
        next = current + i
        if next > 100:          # 규칙: 100을 넘어가면 이동할 수 없다.
            continue
        if roads[next] != 0:    # 규칙: 사다리 또는 뱀을 만나면 무조건 이용해야 한다.
            next = roads[next]
        if board[next] == 0:    # 중복 방문을 방지한다.
            board[next] = board[current] + 1
            queue.append(next)
