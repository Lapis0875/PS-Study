from heapq import heappush, heappop
input = open(0).readline

N = int(input())
pq = []
for _ in range(N):
    for num in map(int, input().split()):
        if len(pq) < N:
            heappush(pq, num)
        elif pq[0] < num:
            heappop(pq)
            heappush(pq, num)

print(pq[0])
