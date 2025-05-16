input = open(0).readline
N = int(input())
ICE_CREAM = {}
for ice in map(int, input().split()):
    try:
        ICE_CREAM[ice] += 1
    except KeyError:
        ICE_CREAM[ice] = 1

Q = int(input())
for _ in range(Q):
    a_i, *A = map(int, input().split())
    b_i, *B = map(int, input().split())
    a = {}
    for ice in A:
        try:
            a[ice] += 1
        except KeyError:
            a[ice] = 1
    if all(ICE_CREAM.get(ice, 0) >= a[ice] for ice in a): # 모든 아이스크림이 존재하는지 확인
        for ice in a:
            ICE_CREAM[ice] -= a[ice]
            if ICE_CREAM[ice] == 0:
                del ICE_CREAM[ice]
        for ice in B:
            try:
                ICE_CREAM[ice] += 1
            except KeyError:
                ICE_CREAM[ice] = 1

res = []
for ice in ICE_CREAM:
    for _ in range(ICE_CREAM[ice]):
        res.append(str(ice))
print(len(res))
if ICE_CREAM:
    print(" ".join(res))