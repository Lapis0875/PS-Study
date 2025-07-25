from collections import deque
input = open(0).readline
text = input().strip()
bomb = input().strip()
text_len = len(text)
bomb_len = len(bomb)

stack = deque()
i = 0
s = 0
while i < text_len:
    stack.append(text[i])

    # 현재 스택의 맨 끝에 폭발 문자열이 있는지 검사
    b_i = bomb_len - 1
    s_i = s
    while s >= bomb_len - 1 and  b_i >= 0:
        if stack[s_i] != bomb[b_i]:
            break
        s_i -= 1
        b_i -= 1
    if b_i < 0:
        # 문자열 폭발!
        for _ in range(bomb_len):
            stack.pop()
            s -= 1
    i += 1
    s += 1

print("".join(stack) if stack else "FRULA")