from sys import stdin

A: int
B: int
while True:
    line: str = stdin.readline()
    if line == "0 0\n":
        break
    A, B = map(int, line.split())
    # C를 A보다 무조건적으로 작은 값으로 잡으면, A가 중앙값이 된다.
    # A를 중앙값이자 평균으로 하려면,
    # (A + B + C) / 3 = A
    # C에 대해 정리하면, C = 2A - B
    print(2 * A - B)