input = open(0).readline
N = int(input())
min_length = 1
numbers = [input().strip() for _ in range(N)]
number_len = len(numbers[0])

s = set()
for i in range(1, number_len + 1):
    for n in numbers:
        s.add(n[-i:])
    if len(s) == N: # 뒤에서 i개까지 자른 부분 문자열이 N개의 학생 번호에 대해 모두 다를 때
        min_length = i
        break
    s.clear()
print(min_length)
# 78%에서 틀림.