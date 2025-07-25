from collections import deque
input = open(0).readline
A, B = map(int, input().split())
queue = deque(((A, 1),))
while queue:
    x, count = queue.popleft()
    if x == B:
        print(count)
        break
    if x * 2 <= B:
        queue.append((x * 2, count + 1))
    if x * 10 + 1 <= B:
        queue.append((x * 10 + 1, count + 1))
    count += 1
else:
    print(-1)