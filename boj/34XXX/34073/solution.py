input = open(0).readline
N = int(input())
words = input().rstrip().split()

for i in range(N - 1):
    print(words[i] + "DORO ", end="")
print(words[N - 1] + "DORO")
