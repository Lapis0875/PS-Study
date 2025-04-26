from sys import stdin

S = int(stdin.readline().strip())
M_a, F_ab, M_b = map(int, stdin.readline().strip().split())
if S <= 240 or S <= M_a + F_ab + M_b:
    print("high speed rail")
else:
    print("flight")
