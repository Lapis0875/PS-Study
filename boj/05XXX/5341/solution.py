input = open(0).readline
while True:
    n = int(input())
    if n == 0:
        break
    print(n * (n + 1) // 2)
