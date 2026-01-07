input = open(0).readline

N = int(input())
arr = [None] * N
total = 0 # 전체 인구만 별도로 합산
for i in range(N):
    arr[i] = tuple(map(int, input().split()))
    total += arr[i][1]

arr.sort(key=lambda e: e[0]) # 좌표를 기준으로 오름차순 정렬

half_people = (total + 1) // 2 # 홀/짝 모두 상관없이 절반 이상이 되는 지점을 찾기 위함
lsum = 0
for i in range(N):
    lsum += arr[i][1]
    if lsum >= half_people:
        print(arr[i][0])
        break
