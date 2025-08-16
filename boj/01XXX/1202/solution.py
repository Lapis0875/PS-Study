from heapq import heappush, heappop
input = open(0).readline

gems = [] # (M, V)
N, K = map(int, input().split())

for _ in range(N):
    m, v = map(int, input().split())
    gems.append((m, v))

gems.sort(key=lambda g: g[0])
bag_weights = sorted(int(input()) for _ in range(K))
bags = []
res = 0

gem_idx = 0
bag_size = 0
for bag_idx in range(K):
    while gem_idx < N and gems[gem_idx][0] <= bag_weights[bag_idx]:
        v = gems[gem_idx][1]
        heappush(bags, (-v, v)) # Sort based on gem's value. (decreasing order)
        gem_idx += 1
        bag_size += 1
    if bag_size > 0:
        _, max_gem = heappop(bags) # Last element : Max Value
        res += max_gem
        bag_size -= 1

print(res)
