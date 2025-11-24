input = open(0).readline

N = int(input())
data = []
for _ in range(N):
    data.append(tuple(map(int, input().split()))) # 도착하는 시각, 수속 처리에 걸리는 시간

data.sort(key = lambda x: x[0]) # 도착 시각 기준 오름차순 정렬

current_time = 0
for arrive_time, process_time in data:
    if current_time < arrive_time: # 마지막 소가 입장한 뒤로 시간이 더 지나서 새로운 소가 도착한 경우
        current_time = arrive_time + process_time
    else:
        current_time += process_time # 이전 소가 입장할 때 까지 기다린 뒤 자신의 입장 절차를 밟는다.

print(current_time)