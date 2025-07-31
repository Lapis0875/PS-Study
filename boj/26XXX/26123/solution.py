input = open(0).readline
N, D = map(int, input().split())
heights = {}
max_height = 0
for height in map(int, input().split()):
    if height > max_height:
        max_height = height
    try:
        heights[height] += 1
    except KeyError:
        heights[height] = 1

count = 0
for day in range(D):
    count += heights[max_height]
    try:
        heights[max_height - 1] += heights[max_height]
    except KeyError:
        if max_height - 1 == 0: # 모든 건물의 높이가 0이 되면 더 이상 레이저를 쏘지 않는다. 
            break
        heights[max_height - 1] = heights[max_height]
    del heights[max_height]
    max_height -= 1

print(count)
