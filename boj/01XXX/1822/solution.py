input = open(0).readline
cnt_a , cnt_b = map(int, input().split())
set_a = {}
for n in map(int, input().split()):
    set_a[n] = True

for n in map(int, input().split()):
    if set_a.get(n, False): # B에 있는 원소가 A에도 있으면
        set_a[n] = False # False로 기록
    # 이 과정을 반복한 뒤 set_a에 True로 남아있는 원소의 개수가 A-B의 원소 개수

res = []
for number in set_a:
    if set_a[number]:
        res.append(number)
res.sort()
print(len(res))
print(" ".join(map(str, res)))