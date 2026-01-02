from heapq import heappush, heappop

lower_half = [] # 작은 수들은 최대 힙으로 관리한다. (항상 큐 안에서 제일 큰 수가 큐의 첫 원소로 오도록 하기 위함.)
upper_half = [] # 큰 수들은 최소 힙으로 관리한다.  
medians = [0] * 5000 # 최대 5000개의 중앙값을 저장할 수 있다.

def add_number(num):
    if len(lower_half) == 0 or num <= -lower_half[0]:
        heappush(lower_half, -num) # heapq는 최소 힙으로 구현되어있으므로, 최대 힙으로 동작시키려면 음수로 저장해야 한다.
    else:
        heappush(upper_half, num)

    # 두 힙의 균형을 맞춘다. (항상 두 힙의 크기 차이는 0 또는 1이어야 한다.)
    if len(lower_half) > len(upper_half) + 1:
        heappush(upper_half, -heappop(lower_half)) # 작은 쪽 큐의 최댓값을 큰 쪽 큐로 이동시킨다.
    elif len(upper_half) > len(lower_half) + 1:
        heappush(lower_half, -heappop(upper_half)) # 큰 쪽 큐의 최솟값을 작은 쪽 큐로 이동시킨다.

def get_median():
    if len(lower_half) > len(upper_half):
        return -lower_half[0]
    elif len(upper_half) > len(lower_half):
        return upper_half[0]
    else:
        return -lower_half[0]  # 짝수 개일 때는 작은 쪽의 최댓값을 반환한다.

def solve():
    lower_half.clear()
    upper_half.clear()
    N = int(input())
    res_size = (N + 1) // 2

    start = 0
    while N > 0:
        stream = map(int, input().split())
        for i, v in enumerate(stream, start=start):
            add_number(v)
            if i % 2 == 0: # 인덱스가 짝수일 때 (홀수 번째)
                medians[i // 2] = get_median()
        start += 10
        N -= 10
    
    start = 0
    print(res_size)
    while start < res_size:
        end = min(start + 10, res_size)
        print(' '.join(map(str, medians[start:end])))
        start += 10

input = open(0).readline
for _ in range(int(input())):
    solve()