input = open(0).readline
arr = list(map(int, input().strip().split()))

def swap(i, j):
    arr[i], arr[j] = arr[j], arr[i]
    print(*arr)

for i in range(5):
    for j in range(5 - i - 1):
        if arr[j] > arr[j + 1]:
            swap(j, j + 1)
