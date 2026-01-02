input = open(0).readline

fun = 0
prev = [0, 0]
for _ in range(int(input())):
    l, r = map(int, input().split())
    if l != 0 and l == prev[0]:
        fun += 1
    if r != 0 and r == prev[1]:
        fun += 1
    if l != 0 and l == r:
        fun += 1
    prev[0] = l
    prev[1] = r

print(fun)
