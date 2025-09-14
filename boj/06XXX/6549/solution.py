input = open(0).readline
HEIGHT_LIMIT = 1_000_000_001

heights = [0] * 100_000
def divide_and_conquer(s, e):
    if s == e:
        return heights[s]

    mid = (s + e) // 2
    left_surface = divide_and_conquer(s, mid)
    right_surface = divide_and_conquer(mid + 1, e)

    min_height = HEIGHT_LIMIT
    answer = 0
    l = mid
    r = mid + 1
    while s <= l and r <= e:
        min_height = min(min_height, heights[l], heights[r])
        answer = max(answer, min_height * (r - l + 1)) # 기존에 구한 최대 면적과 현재 범위 내의 최대 면적 중 최댓값 사용

        if l == s:
            r += 1
        elif r == e:
            l -= 1
        elif heights[l - 1] < heights[r + 1]:
            r += 1
        else:
            l -= 1
    return max(answer, left_surface, right_surface)

while True:
    hist_text = input().rstrip()
    if hist_text == "0":
        break

    hist = map(int, hist_text.split())
    N = next(hist)
    for i, h in enumerate(hist):
        heights[i] = h
    
    print(divide_and_conquer(0, N - 1))