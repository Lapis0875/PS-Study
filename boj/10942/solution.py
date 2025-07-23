input = open(0).readline
N = int(input())
arr = list(map(int, input().split()))
DP = [[-1] * 2000 for _ in range(2000)]

for i in range(N):
    DP[i][i] = 1

def check_palindrome(s, e):
    if s >= e:
        return 1
    if DP[s][e] == -1:
        DP[s][e] = int(check_palindrome(s + 1, e - 1) == 1 and arr[s] == arr[e])

    return DP[s][e]

for _ in range(int(input())):
    S, E = map(lambda x: int(x) - 1, input().split())
    print(check_palindrome(S, E))