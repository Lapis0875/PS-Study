input = open(0).readline

box = [0] * 1000
for _ in range(int(input())):
    J, N = map(int, input().split())
    for i in range(N):
        R, C = map(int, input().split())
        box[i] = R * C
    box.sort(reverse=True)
    idx = 0
    while J > 0 and idx < N:
        J -= box[idx]
        idx += 1
    print(idx)