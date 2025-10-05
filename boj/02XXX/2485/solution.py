input = open(0).readline
N = int(input())
distance = [0] * (N - 1)

prev = int(input())
for i in range(N - 1):
    cur = int(input())
    distance[i] = cur - prev
    prev = cur

def gcd(a, b):
    while b > 0:
        a, b = b, a % b
    return a

distance.sort(reverse=True)
base = distance[0]
for i in range(1, N - 1):
    base = gcd(base, distance[i])

ans = 0
for i in range(N - 1):
    ans += distance[i] // base - 1

print(ans)