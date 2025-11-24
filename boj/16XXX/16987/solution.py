input = open(0).readline
N = int(input())
EGGS = list(list(map(int, input().split())) for _ in range(N))
# EGGS = [DURABILITY, WEIGHT]
DURABILITY = 0
WEIGHT = 1

def dfs(holding):
    if holding == N: # 가장 오른쪽에 위치한 계란을 들 때 종료
        cnt = 0
        for egg in EGGS:
            if egg[DURABILITY] <= 0:
                cnt += 1
        return cnt
    
    if EGGS[holding][DURABILITY] <= 0:
        return dfs(holding + 1)
    
    cnt = 0
    hit = False
    # 다른 계란을 치는 경우
    for i in range(N):
        cur_durability, cur_weight = EGGS[holding]
        other_durability, other_weight = EGGS[i]
        # 들고있는 계란을 치는 경우 / 치려는 계란이 이미 깨진 경우는 DFS를 진행하지 않는다.
        if i == holding or other_durability <= 0: 
            continue

        EGGS[holding][DURABILITY] -= other_weight
        EGGS[i][DURABILITY] -= cur_weight
        hit = True
        res = dfs(holding + 1)
        if res > cnt:
            cnt = res
        EGGS[holding][DURABILITY] = cur_durability
        EGGS[i][DURABILITY] = other_durability
    
    # 아무것도 깨지 않고 다음 계란으로 넘어갔을 경우
    if not hit:
        res = dfs(holding + 1)
        if res > cnt:
            cnt = res
    return cnt

print(dfs(0))