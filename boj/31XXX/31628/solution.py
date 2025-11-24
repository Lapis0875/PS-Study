input = open(0).readline
data = [input().rstrip().split() for _ in range(10)]

prev = ""
found = False
for row in range(10):
    prev = data[row][0]
    for col in range(1, 10):
        if data[row][col] != prev:
            break
    else:
        found = True
for col in range(10):
    prev = data[0][col]
    for row in range(1, 10):
        if data[row][col] != prev:
            break
    else:
        found = True

print("1" if found else "0")
