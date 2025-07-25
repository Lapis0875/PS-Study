input = open(0).readline
ISBN = list(map(lambda x: -1 if x == "*" else int(x), input().strip()))

total = 0
idx = 0
for i in range(13):
    if ISBN[i] == -1:
        idx = i
        continue
    if i % 2 == 1:
        total += 3 * ISBN[i]
    else:
        total += ISBN[i]

for i in range(10):
    if (idx % 2 == 1 and (total + 3 * i) % 10 == 0) or (idx % 2 == 0 and (total + i) % 10 == 0):
        print(i)
        break