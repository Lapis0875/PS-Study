from sys import stdin
from collections import deque

N: int = int(stdin.readline())
students: deque[int] = deque(map(int, stdin.readline().split()))
waiting: deque[int] = deque()
after: deque[int] = deque()

now: int = 1                                                # 현재 간식을 받아야 하는 번호
loop: bool = True
while students:
    head: int = students.popleft()
    if head == now:
        after.append(head)
        now += 1
    elif waiting and waiting[-1] == now:
        after.append(waiting.pop())
        now += 1
    else:
        waiting.append(head)

while waiting:
    after.append(waiting.pop())

prev: int = 0
while after:
    i: int = after.popleft()
    if prev > i:
        print("Sad")
        break
    prev = i
else:
    print("Nice")
