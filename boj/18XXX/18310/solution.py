input = open(0).readline

N = int(input())
arr = sorted(map(int, input().split()))

print(arr[(N - 1) // 2]) # 배열의 인덱스는 1 작기 때문에