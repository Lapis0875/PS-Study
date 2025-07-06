input = open(0).readline
N = int(input())
liquids = list(map(int, input().split()))

l = 0
r = N - 1
min_value = 1_000_000_000_001
min_pair = [None, None]
while l < r:
    m = liquids[l] + liquids[r]
    if abs(m) < abs(min_value):
        min_value = m
        min_pair[0] = liquids[l]
        min_pair[1] = liquids[r]
    
    if m > 0:
        r -= 1
    elif m < 0:
        l += 1
    else:
        break

print(*min_pair)