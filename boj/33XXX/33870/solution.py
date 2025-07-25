input = open(0).readline
N, M = map(int, input().split())
DURATION = tuple(map(int, input().split()))
PLAN = tuple(map(lambda x: int(x) - 1, input().split()))    # 배열 인덱스에 맞게 1 줄인다.

tangled = [False for _ in range(N)]
combed = [0 for _ in range(N)]  # 양의 정수: 빗질하고 아직 여유가 있음. / 0: 기한 안에 빗질을 안한 상태. 이 상태에서 빗질을 해도 엉킴. / 음의 정수: 엉켜있음. 2일 연속 빗질 시 DURATION[i]로 초기화.
for day in range(1, M + 1): # 1일차부터 M일차까지 순회하면서...
    for i in range(N):
        if not tangled[i] and day -  combed[i] > DURATION[i]:
            tangled[i] = True

    dog = PLAN[day - 1] # 오늘 빗질할 개
    if tangled[dog] and combed[dog] == day - 1:  # 엉킨 상태이며 2일 연속으로 빗질했다면
        tangled[dog] = False
    combed[dog] = day  # 오늘 빗질한 개의 상태를 갱신한다.

cnt = 0
for i in range(N):
    if not tangled[i] and M + 1 -  combed[i] > DURATION[i]:
        tangled[i] = True
    if tangled[i]:
        cnt += 1
print(cnt)
