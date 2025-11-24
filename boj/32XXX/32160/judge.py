# input
N = int(input())
# solution output
ans = int(input())
res = []
while True:
    line = input().strip()
    if line == "":
        break
    res.append(tuple(map(int, line.split())))

if len(res) != N - 1:
    print(f"Wrong Answer: 연산의 개수가 {N-1}개가 아님 ({len(res)}개)")
    exit(0)

# judge
board = {i: 1 for i in range(1, N + 1)}

for a, b in res:
    try:
        board[a] -= 1
    except KeyError:
        print(f"Wrong Answer: 칠판에 적히지 않은 수 {a}를 연산에 사용함.")
    
    try:
        board[b] -= 1
    except KeyError:
        print(f"Wrong Answer: 칠판에 적히지 않은 수 {b}를 연산에 사용함.")
    
    if board.get(a, -1) == 0:
        del board[a]
    if board.get(b, -1) == 0:
        del board[b]
    
    try:
        board[abs(a - b)] += 1
    except KeyError:
        board[abs(a - b)] = 1

traced_res = 0
for k in board:
    traced_res = max(traced_res, k)

print(f"Accepted: {ans}")
print(f"Re-calculated: {traced_res}")
print(f"Valid? : {ans == traced_res and len(board) == 1}")
    