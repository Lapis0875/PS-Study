from sys import stdin

N, M = map(int, stdin.readline().split())

numbers = map(int, stdin.readline().split())
sum_arr: list[int] = [0, next(numbers)]

for num in numbers:
    sum_arr.append(sum_arr[-1] + num)

for _ in range(M):
    i, j = map(int, stdin.readline().split())
    print(sum_arr[j] - sum_arr[i - 1])
