input = open(0).readline
N = int(input())
board = {i: 1 for i in range(1, N + 1)}
res = []

def add_to_board(n):
    try:
        board[n] += 1
    except KeyError:
        board[n] = 1

def remove_from_board(n):
    board[n] -= 1
    if board[n] == 0:
        del board[n]

# Step 1. 1 ... N-1의 모든 수를 인접한 수 끼리 빼서 1로 만든다.
number = N - 1
while number >= 2:
    a = number
    b = a - 1
    if a in board and b in board:
        res.append(f"{a} {b}\n")
        remove_from_board(a)
        remove_from_board(b)
        add_to_board(abs(a - b))
    number -= 2

print(board)

# Step 2. 1이 2개 이상 남아있다면, 1을 계속 빼서 0을 만든다.
ones = board.get(1, 0)
if ones > 1:
    res.append("1 1\n" * (ones // 2))
    board[0] = ones >> 1
    board[1] = ones & 1
    if board[1] == 0:
        del board[1]

print(board)

# Step 3. 0이 있다면, 0을 계속 지운다.
zeros = board.get(0, 0)
if zeros > 1:
    res.append("0 0\n" * (zeros - 1))
    board[0] = 1
if board[0] == 0:
    del board[0]

print(board)

# Step 4. 답 찾기
ans = N
# Step 4-1. 1과 0이 모두 있다면 1만 남겨준다.
if board.get(0, 0) == 1 and board.get(1, 0) == 1:
    res.append("1 0\n")
    remove_from_board(0)

# 0이 남아있을 경우 답은 N
if board.get(0, 0) > 0:
    res.append(f"{N} 0\n")
    remove_from_board(0)
# 1이 남아있을 경우 답은 N - 1
elif board.get(1, 0) > 0 and N > 1:
    res.append(f"{N} 1\n")
    remove_from_board(1)
    remove_from_board(N)
    add_to_board(N - 1)
    ans = N - 1

print(ans)
print("".join(res))
    