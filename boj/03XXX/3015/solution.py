from collections import deque
input = open(0).readline

stack = deque() # [해당 사람의 키, 키가 같은 연속되는 사람의 수]
N = int(input())
heights = tuple(int(input()) for _ in range(N))
pairs = 0

# 스택에 저장된 값들은 스택의 최상단부터 아래로 갈수록 커진다 (더 작은 값을 새로 추가하게 됨.)
for cur_height in heights:
    while stack and stack[0][0] < cur_height:
        # 현재 스택의 최상단에 위치한 키가 비교하는 키(cur_height)보다 작을 동안 계속 스택에서 뺀다.
        # 이들은 키가 cur_height보다 작기 때문에 cur_height 다음 사람을 볼 수 없음이 자명함
        x, count = stack.popleft()
        pairs += count # 해당 키를 가진 인원이 연속으로 있는 수 만큼 더해준다.
    if len(stack) == 0:
        stack.appendleft((cur_height, 1))
    elif stack[0][0] == cur_height: # 현재 스택의 최상단에 있는 사람의 키가 비교하려는 키와 같은 경우
        height, count = stack.popleft()
        pairs += count # 현재 스택의 위에 위치한 키의 사람들의 수 만큼 쌍이 더 생긴다.
        if len(stack) > 0: # 스택에 그 다음 사람이 있는 경우, 마찬가지로 한 쌍이 더 생긴다. ( 이 경우, )
            pairs += 1 # 왜 한 쌍만 더 생기냐? stack[1] or stack[0]의 나머지 사람들 >= stack[0] > cur_height가 되므로 stack[0]의 제일 끝쪽 사람 외에는 쌍을 이루지 못한다.
        stack.appendleft((height, count + 1))
    else: # 현재 스택의 위에 위치한 키보다 비교하는 키(cur_height)가 더 작은 경우
        stack.appendleft((cur_height, 1))
        pairs += 1 # 스택의 다음 값들과는 쌍을 이루지 못한다. (stack[1] > stack[0] > cur_height 이기 때문.)

print(pairs)