input = open(0).readline
pyramids = [0, 1]
# i=0   cnt=0   
# i=1   cnt=1   1
# i=2   cnt=3   1 2 1
# i=3   cnt=5   1 2 3 2 1
# i=4   cnt=7   1 2 3 4 3 2 1 = 1 2 3 2 1 / 4 / 3 = pyramids[i-1] + i-1 + i
# cnt[i] = 2 * i - 1 / dist[i] = dist[i-1] + i - 1 # 굳이 점화식 안써도 어짜피 캐싱해두고 구할거라 이게 빠름.
for _ in range(int(input().strip())):
    X, Y = map(int, input().split())
    goal_dist = Y - X

    i = 1
    cnt = 0
    while pyramids[i] < goal_dist:
        i += 1
        if len(pyramids) <= i:
            for j in range(len(pyramids), i + 1):
                pyramids.append(pyramids[j - 1] + 2 * j - 1)
    # while문 종료 이후의 i는 목표 거리를 넘거나 같은 최소의 i값으로, i-1의 이동 거리에 추가 이동 횟수를 더해 조절하면 된다.
    if pyramids[i] == goal_dist:
        print(2 * i - 1)
        continue

    base_dist = pyramids[i - 1]
    cnt = 2 * i - 3      # 2 * (i-1) - 1 = 2 *  - 3
    dist = i - 1
    while base_dist < goal_dist and dist > 0:
        while base_dist + dist <= goal_dist:
            base_dist += dist
            cnt += 1
        dist -= 1
    print(cnt)