input = open(0).readline
S, P = map(int, input().split())

DNA = input().strip()
required = tuple(map(int, input().split()))
window = [0, 0, 0, 0]

def count_char_to_window(char, diff):
    if char == 'A':
        window[0] += diff
    elif char == 'C':
        window[1] += diff
    elif char == 'G':
        window[2] += diff
    else:  # char == 'T'
        window[3] += diff

# window의 크기만큼 처음 P - 1개의 문자를 미리 센다.
count = 0
for i in range(P):
    count_char_to_window(DNA[i], 1)
    
for i in range(4):
    if window[i] < required[i]:
        break
else:
    count += 1

for i in range(1, S - P + 1): # 직관적인 이해를 위해, i부터 길이 P의 윈도우를 생각하자.
    count_char_to_window(DNA[i - 1], -1)        # 가장 오래된 문자 제거
    count_char_to_window(DNA[i + P - 1], +1)    # 새로운 문자 추가
    
    for i in range(4):
        if window[i] < required[i]:
            break
    else:
        count += 1

print(count)