input = open(0).readline

N = int(input())
media = tuple(tuple(map(int, input().rstrip())) for _ in range(N))

def quad_tree(r, c, size):
    if size == 1:
        return str(media[r][c])
    
    res = ""
    prev = media[r][c]
    for dr in range(size):
        for dc in range(size):
            if media[r + dr][c + dc] != prev:
                # 이 조각을 다시 4등분해 출력해야 한다.
                res += "("
                half = size // 2
                res += quad_tree(r, c, half)
                res += quad_tree(r, c + half, half)
                res += quad_tree(r + half, c, half)
                res += quad_tree(r + half, c + half, half)
                res += ")"
                return res
    else:
        return str(prev)

print(quad_tree(0, 0, N))