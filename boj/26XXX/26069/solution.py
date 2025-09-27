input = open(0).readline
N = int(input())
rainbow_dancing = {"ChongChong": True}

for _ in range(N):
    a, b = input().rstrip().split()
    if rainbow_dancing.get(a, False) or rainbow_dancing.get(b, False):
        rainbow_dancing[a] = True
        rainbow_dancing[b] = True

print(len(rainbow_dancing))