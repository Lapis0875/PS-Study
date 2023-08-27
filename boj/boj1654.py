from sys import stdin

K, N = map(int, stdin.readline().split())

lans: list[int] = []
totalLen: int = 0
for _ in range(K):
    lan: int = int(stdin.readline())
    lans.append(lan)
    totalLen += lan

# Binary Search
left: int = 1
right: int = totalLen // N
answer: int = -1

while left <= right:
    mid: int = (left + right) // 2
    count: int = 0

    for i in range(K):
        count += lans[i] // mid
    
    if count >= N:
        left = mid + 1
        if (mid > answer):
            answer = mid
    else:
        right = mid - 1

print(answer)