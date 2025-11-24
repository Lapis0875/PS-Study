from functools import cmp_to_key

input = open(0).readline
N, M = map(int, input().split())
words = {}

# 1. 단어 등장 횟수 기록
for _ in range(N):
    word = input().rstrip()
    if len(word) < M:
        continue

    try:
        words[word] += 1
    except KeyError:
        words[word] = 1

# 2. 정렬 기준 함수
# 1) 자주 나올 수록 앞으로
# 2) 길 수록 앞으로
# 3) 사전 순으로 앞설 수록 앞으로
def compare_words(a, b):
    if words[a] != words[b]:
        return words[b] - words[a]
    if len(a) != len(b):
        return len(b) - len(a)
    if a < b:
        return -1
    elif a > b:
        return 1
    else:
        return 0

# 3. 정렬 후 출력
sorted_words = sorted(words.keys(), key=cmp_to_key(compare_words))
for word in sorted_words:
    print(word)
