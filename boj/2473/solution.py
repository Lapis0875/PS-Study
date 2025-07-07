input = open(0).readline
N = int(input())
liquids = sorted(map(int, input().split()))

if N == 3:
    print(*liquids)
    exit(0)

def binary_search(n, start_index):
    l = start_index
    r = N - 1
    while l <= r:
        mid = (l + r) // 2
        if liquids[mid] < n:
            l = mid + 1
        elif liquids[mid] > n:
            r = mid - 1
        else:
            return mid

    # 정확한 값을 배열 안에서 찾지 못한 경우, 근사값을 반환한다.
    if l >= N: # 범위 밖이 탐색된 경우
        return r
    elif r < 0:
        return l
    else:
        return l if abs(liquids[r] + n) > abs(liquids[l] + n) else r


# l, r을 정해두고 m을 매개변수 탐색
# 기준이 되는 조건? : l + m + r의 절댓값이 가장 작아지는 경우?
print(liquids)
l = 0
r = N - 1
min_value = 1_000_000_000_001
min_pair = [None, None, None]
for l in range(N - 2):
    m = l + 1
    r = N - 1
    while l < m and m < r  and r < N:
        cur_value = liquids[l] + liquids[m] + liquids[r]
        print(f"liquids: {liquids[l]} {liquids[m]} {liquids[r]}")
        print(f"농도: {cur_value}")
        if abs(cur_value) < min_value:
            print("-> 농도 갱신")
            min_value = abs(cur_value)
            min_pair[0] = liquids[l]
            min_pair[1] = liquids[m]
            min_pair[2] = liquids[r]
    
        if cur_value > 0:
            r -= 1
        elif cur_value < 0:
            m += 1
        else:
            break
            

print(*min_pair)