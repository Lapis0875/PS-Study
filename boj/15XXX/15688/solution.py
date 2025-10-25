input = open(0).readline

count = {}
N = int(input())
for _ in range(N):
    i = int(input())
    try:
        count[i] += 1
    except KeyError:
        count[i] = 1

for i in sorted(count.keys()):
    print(f"{i}\n" *count[i], end="")
