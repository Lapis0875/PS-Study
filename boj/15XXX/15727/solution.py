input = open(0).readline
L = int(input())
time = L // 5
if L % 5:
    time += 1
print(time)