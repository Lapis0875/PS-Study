input = open(0).readline
N = int(input().strip())
SUB_ROOMS = list(map(int, input().strip().split()))
CONTINUOUS_ZERO_SUBROOMS = []

ants = sum(SUB_ROOMS)   # 먼저 모든 쪽방을 다 사용한다. (쪽방이 있는 본 방이 인접해도 쪽방끼리는 상관 없다.)
if ants == 0: # 쪽방이 하나도 없다면
    print((N - 1) // 2 + 1 if N % 2 == 0 else (N - 1) // 2)
    exit()

start = -1
for i in range(N):
    if start == -1:
        if SUB_ROOMS[i] == 0:
            start = i
        else:
            CONTINUOUS_ZERO_SUBROOMS.append((start, i - 1))
            start = -1
if start != -1:
    if SUB_ROOMS[0] == 0 and len(CONTINUOUS_ZERO_SUBROOMS) > 0:
        s, e = CONTINUOUS_ZERO_SUBROOMS[0]
        CONTINUOUS_ZERO_SUBROOMS.append((start, N + e))
        CONTINUOUS_ZERO_SUBROOMS.pop(0) # 첫 번째 쪽방은 마지막 쪽방과 연결되어 있으므로 제거
    else:
        CONTINUOUS_ZERO_SUBROOMS.append((start, N - 1))

for s, e in CONTINUOUS_ZERO_SUBROOMS:
    if s == e:
        ants += 1
    else:
        length = e - s + 1
        ants += length // 2
        if length % 2 == 1:
            ants += 1

print(ants)