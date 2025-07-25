input = open(0).readline
N, X, Y = map(int, input().strip().split())

fixed = Y - X - 1

array = [0 for _ in range(2 * N + 1)]   # 1~2N번 인덱스까지 사용. (0번 미사용)
array[X] = array[Y] = fixed
cnt = 0

def dfs(depth):
    global cnt
    if depth == fixed:          # 이미 배치되어 있으므로 스킵.
        return dfs(depth + 1)
    if depth == N + 1:
        cnt += 1
        # print(array)    # DEBUG
        return

    for i in range(1, 2 * N - depth):   # len(array) - (depth + 1) = 2*N+1 - depth - 1 = 2*N - depth
        if array[i] == 0 and array[i + depth + 1] == 0:
            array[i] = array[i + depth + 1] = depth
            dfs(depth + 1)
            array[i] = array[i + depth + 1] = 0

dfs(1)
print(cnt)