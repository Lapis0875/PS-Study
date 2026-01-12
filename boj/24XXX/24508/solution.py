input = open(0).readline

N, K, T = map(int, input().split())
nadories = sorted(map(int, input().split()), reverse=True)
total_nadories = sum(nadories)

s = 0
e = N - 1
popped = 0
while s < e:
    while T > 0 and nadories[e] > 0 and nadories[s] < K:
        T -= 1
        nadories[e] -= 1
        nadories[s] += 1
    
    if nadories[s] == K:
        s += 1
        popped += K
    if nadories[e] == 0:
        e -= 1
    
    if T == 0:
        break

print("YES" if popped == total_nadories else "NO")
