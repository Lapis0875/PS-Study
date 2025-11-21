input = open(0).readline

S = [] # 숫자를 고를 집합
K = 0 # 집합 S의 원소의 개수
used = [False] * 12 # 6 < k < 13
selected = [0] * 6 # 독일 로또는 6개의 숫자로 구성됨

def select_numbers(depth, prev_num_idx):
    global K
    if depth == 6:
        print(*selected)
        return
    
    for i in range(prev_num_idx + 1, K):
        if not used[i]:
            selected[depth] = S[i]
            used[i] = True
            select_numbers(depth + 1, i)
            used[i] = False
    selected[depth] = 0

while True:
    line = input().rstrip()
    if line[0] == "0":
        break

    K, *S = map(int, line.split())
    for i in range(K):
        if i < 6:
            selected[i] = 0
        used[i] = False
    select_numbers(0, -1)
    print()
