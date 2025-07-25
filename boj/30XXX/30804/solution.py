input = open(0).readline
N = int(input())
fruits = tuple(map(int, input().split()))
max_length = 0
left = 0
count = {}
for right in range(N):
    try:
        count[fruits[right]] += 1
    except KeyError:
        count[fruits[right]] = 1
    while len(count) > 2:
        count[fruits[left]] -= 1
        if count[fruits[left]] == 0:
            del count[fruits[left]]
        left += 1
    max_length = max(max_length, right - left + 1)
print(max_length)
