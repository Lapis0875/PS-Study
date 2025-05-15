input = open(0).readline
L, N, T = map(int, input().split())
world = [-1 for _ in range(L + 1)]      # world[0]과 world[L]은 각각 벽. 배열의 값은 그 위치에 있는 공의 번호.
balls = []                              # balls[[pos, direction]]는 i번 공의 위치와 방향을 각각 기록한다. 

for i in range(N):
    x, d = input().strip().split()
    x = int(x)
    balls.append([x, -1 if d == "L" else 1])
    world[x] = i

count = 0
for t in range(T):  # 1~T초 동안 공을 이동시킨다.
    for idx in range(N):
        pos, direction = balls[idx]
        world[pos] = -1
        new_pos = pos + direction
        if new_pos == 0 or new_pos == L:    # 벽에 부딪히면 방향만 바꾼다.
            balls[idx][1] *= -1
        elif world[new_pos] != -1:          # 다른 공과 부딪히면 두 공의 방향을 바꾸고 충돌 횟수를 기록한다.
            balls[idx][1] *= -1
            count += 1
            other_ball = world[new_pos]
            balls[other_ball][1] *= -1
        world[new_pos] = idx
        balls[idx][0] = new_pos
print(count)