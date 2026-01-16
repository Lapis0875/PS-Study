input = open(0).readline

N = int(input())
answer_cnt = [0] * (51)
for cnt in map(int, input().split()):
    answer_cnt[cnt] += 1

res = -1
for ans in range(51):
    if ans == answer_cnt[ans]:
        res = ans

print(res)
