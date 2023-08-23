X: int = int(input())
count: int = 0
for i in range(7):
    if X & (1 << i):
        count += 1
print(count)
