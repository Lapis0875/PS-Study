from sys import stdin

N, M = map(int, stdin.readline().split())
s_x, s_y = map(int, stdin.readline().split())
e_x, e_y = map(int, stdin.readline().split())

if N == 1 or M == 1:        # 비숍은 대각선으로만 이동할 수 있으므로, 일자형 보드에서는 이동 자체가 불가능하다.
    print("YES" if s_x == e_x and s_y == e_y else "NO")
else:
    print("NO" if ((e_x - s_x) + (e_y - s_y)) % 2 == 1 else "YES")
