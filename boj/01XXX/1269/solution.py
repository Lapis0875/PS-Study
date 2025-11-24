input = open(0).readline
input() # 굳이 필요하지 않은 입력 값

A = set()
B = set()
for i in map(int, input().split()):
    A.add(i)
for i in map(int, input().split()):
    B.add(i)

print(len((A - B) | (B - A)))