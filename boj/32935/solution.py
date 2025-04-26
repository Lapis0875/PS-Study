from sys import stdin

N = int(stdin.readline().strip())
array = list(map(int, stdin.readline().strip().split()))
S = sum(array)
array.sort()
S_2 = -array[0]
print(S_2 if S_2 > S else S)
