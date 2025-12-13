from collections import deque
input = open(0).readline
S = input().rstrip()
T = input().rstrip()

word_info = {chr(97 + c): deque() for c in range(26)}
for i, c in enumerate(S):
    word_info[c].append(i)

cnt = 0
can_make = True
while can_make:
    for t_idx in range(len(T)):
        c = T[t_idx]
        if len(word_info[c]) == 0: # T의 문자가 S에 없는 경우
            can_make = False
            break

        pos = word_info[c].popleft()
        if t_idx < len(T) - 1:
            next_c = T[t_idx + 1]
            if len(word_info[next_c]) == 0: # 다음 차례의 문자가 S에 없는 경우
                can_make = False
                break

            while word_info[next_c][0] <= pos: # 다음 차례의 문자가 현재 문자보다 앞에 있을 경우 조건에 맞지 않는다.
                # 이 경우 next_c의 이번 요소는 조합에 T의 구성에 사용될 수 없으니 버리고 계속 탐색한다.
                word_info[next_c].popleft()
                if len(word_info[next_c]) == 0: # 다음 차례의 문자가 S에 없는 경우
                    can_make = False
                    break

    else: # T의 모든 문자를 한 차례 구성한 경우에만 진입하는 구문
        cnt += 1

print(cnt)