from sys import stdin

N = int(stdin.readline())
a_win = 0
b_win = 0
for _ in range(N):
    A, B = map(int, stdin.readline().split())
    if A > B:
        a_win += 1
    elif A < B:
        b_win += 1
    # 무승부인 경우에는 아무도 승리하지 않는다.

print(a_win, b_win)