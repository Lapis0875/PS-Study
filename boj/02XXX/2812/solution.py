from collections import deque

input = open(0).readline

N, K = map(int, input().split())
number = input().rstrip()

stack = deque()
cur = 0
while cur < N:
    while K > 0 and stack and stack[-1] < number[cur]:
        stack.pop()
        K -= 1
    
    stack.append(number[cur])
    cur += 1

while K > 0: # 앞에서 K보다 덜 지웠을 경우, 끝에서 남은 개수만큼 지워낸다.
    stack.pop()
    K -= 1

print("".join(stack))
