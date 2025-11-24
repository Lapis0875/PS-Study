from heapq import heappush, heappop

input = open(0).readline

max_heap = []
min_heap = []
sum_max_heap = 0
sum_min_heap = 0
sum_b = 0

def add_element(v):
    global sum_max_heap, sum_min_heap
    if len(max_heap) == len(min_heap):
        heappush(max_heap, (-v, v))
        sum_max_heap += v
    else:
        heappush(min_heap, v)
        sum_min_heap += v
    
    if len(max_heap) > 0 and len(min_heap) > 0:
        max_top = max_heap[0][1]
        min_top = min_heap[0]

        if max_top > min_top:
            heappop(max_heap)
            heappop(min_heap)
            heappush(max_heap, (-min_top, min_top))
            heappush(min_heap, max_top)
            sum_max_heap += min_top - max_top
            sum_min_heap += max_top - min_top

for _ in range(int(input())):
    cmd = input().split()
    if cmd[0] == "1":
        a = int(cmd[1])
        b = int(cmd[2])
        sum_b += b
        add_element(a)
        
    else:
        x = max_heap[0][1]
        y = (x * len(max_heap) - sum_max_heap) + (sum_min_heap - x * len(min_heap)) + sum_b
        print(x, y)
