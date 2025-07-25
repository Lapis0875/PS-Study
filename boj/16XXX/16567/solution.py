input = open(0).readline
N, M = map(int, input().split())
road = list(map(int, input().split()))
cnt = 0

# 최초 도로의 상태 확인
checking = False
for i in range(N - 1):
    if not checking and road[i] == 1:
        checking = True
    if checking:
        if road[i + 1] == 0:
            cnt += 1
            checking = False
if checking:
    cnt += 1  # 마지막 그룹이 끝나지 않은 경우

for _ in range(M):
    query = input().strip()
    if query[0] == "0": # 현재 길의 모든 칸을 깨끗하게 만들기 위한 "flip"의 최소 횟수를 하인들에게 크게 외치게 한다.
        print(cnt)
    else:   # 바이너리 길의 i번째 칸을 더럽힌다. 단, 이미 더럽혀져 있다면 아무 일도 일어나지 않는다.
        value = int(query[2:]) - 1
        if road[value] == 1:
            continue

        if value > 1 and road[value - 1] == 1:  # 왼쪽이 더러운 경우
            if value < N - 1 and road[value + 1] == 1:  # 오른쪽도 더러운 경우
                cnt -= 1    # 두 그룹이 하나로 합쳐지므로 개수 감소.
            # 왼쪽만 더럽고 오른쪽은 깨끗한 경우는 기존 그룹에 붙는 것이므로 개수 변화 없음.
        elif value < N - 1 and road[value + 1] == 1:  # 오른쪽이 더러운 경우
            if value > 0 and road[value - 1] == 1:  # 왼쪽도 더러운 경우
                cnt -= 1    # 두 그룹이 하나로 합쳐지므로 개수 감소.
            # 왼쪽만 더럽고 오른쪽은 깨끗한 경우는 기존 그룹에 붙는 것이므로 개수 변화 없음.
        else:  # 양쪽 모두 깨끗한 경우, 새로운 그룹이 생김.
            cnt += 1
        road[value] = 1
