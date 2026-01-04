from heapq import heappush, heappop, heapreplace
from collections import deque
input = open(0).readline
N, M = map(int, input().split())

baits = sorted(map(int, input().split())) # 미끼의 가치를 최소 힙으로 관리한다.
fishes = sorted(map(int, input().split())) # 물고기들의 가치를 최소 힙으로 관리한다.

valid_baits = []
caught_fishes = []

bait_idx = 0
for fish in fishes:
    while bait_idx < N and baits[bait_idx] < fish:
        heappush(valid_baits, -baits[bait_idx]) # 항상 물고기의 가치보다 작은 미끼 중 가장 큰 것을 사용해 이후 남은 물고기를 
        bait_idx += 1
    
    if valid_baits:
        # 사용 가능한 가장 가치가 큰 미끼로 물고기를 낚는다.
        heappop(valid_baits)
        heappush(caught_fishes, fish)
    else:
        # 더 이상 사용할 수 있는 미끼가 없다면 기본 미끼로 물고기를 낚는다.
        if caught_fishes and caught_fishes[0] < fish:
            heapreplace(caught_fishes, fish) # heappop + heappush보다 더 효율적인 방식.

print(sum(caught_fishes))