stdin = open(0)
input = lambda: stdin.readline().rstrip()
for _ in range(int(input())):
    assert input()