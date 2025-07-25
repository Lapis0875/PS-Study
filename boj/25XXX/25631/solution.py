input = open(0).readline

N = int(input())

# 입력으로 주어진 모든 마트료시카를 크기를 기준으로 세어, 가장 많이 중복된 길이의 개수가 결과적으로 합치고 남는 마트료시카와 같다.
counter = {}
res = 0
for a in map(int, input().split()):
    if a in counter:
        counter[a] += 1
    else:
        counter[a] = 1
    res = max(res, counter[a])

print(res)