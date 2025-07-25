input = open(0).readline
N = int(input())

over_half = 0
time = 30
for _ in range(N):
    study_time = int(input())
    if study_time >= time:
        if study_time <= time * 2: # 적어도 절반은 공부했는가?
            over_half += 1
    elif time > study_time:
        over_half += 1
    time = (time - study_time) if time > study_time else 30
print(over_half)