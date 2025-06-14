input = open(0).readline
N, L = map(int, input().strip().split())

ponds = []

for _ in range(N):
    s, e = map(int, input().strip().split())
    ponds.append((s, e))

ponds.sort(key=lambda p: p[0])

last_covered = -1
pond_idx = 0
cnt = 0
while last_covered <= 1_000_000_000 and pond_idx < N:
    s, e = ponds[pond_idx]
    if last_covered >= e:   # 이미 이번 물웅덩이까지 덮인 경우.
        pond_idx += 1
        continue

    elif last_covered >= s:     # 이미 일부가 덮여 있고, 나머지 부분을 덮는 상황.
        needed = e - last_covered
        c = needed // L
        if needed % L > 0:
            c += 1
        last_covered = last_covered + c * L
    
    else:   # 아예 새로 덮는 상황.
        needed = e - s
        c = needed // L
        if needed % L > 0:
            c += 1
        require = c * L
        # 다음번 물웅덩이 범위 고려해서 이번 널빤지가 겹치게 할 수 있다면 그쪽으로 빼고, 아니라면 그냥 왼쪽으로 뺀다.
        if pond_idx < N - 1 and (s + require) >= ponds[pond_idx + 1][0]:
            last_covered = s + require
        elif (e - require) > last_covered:  # 이전 범위로만 튀어나오게 널빤지를 덮을 수 있다.
            last_covered = e
        else:
            last_covered += require
    pond_idx += 1
    cnt += c
print(cnt)