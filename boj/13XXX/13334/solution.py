from heapq import heappush, heappop
input = open(0).readline

N = int(input())
# 1. 모든 좌표를 읽으면서 (작은 값, 큰 값) 형태로 정규화하여 저장
all_people = [tuple(sorted(map(int, input().split()))) for _ in range(N)]

D = int(input())

# 2. 필터링하는 동시에 끝점을 기준으로 정렬
valid_people = sorted(filter(lambda p: p[1] - p[0] <= D, all_people), key=lambda x: x[1])

# 이제 valid_people 리스트로 스위핑 알고리즘을 수행하면 됩니다.
contained_heap = []
max_people = 0

for start, end in valid_people:
    rail_start_limit = end - D
    
    heappush(contained_heap, start)
    
    while contained_heap and contained_heap[0] < rail_start_limit:
        heappop(contained_heap)
    
    max_people = max(max_people, len(contained_heap))

print(max_people)