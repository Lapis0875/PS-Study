input = open(0).readline

def count_pins(depth, N, sum_of_digits, S):
    if depth == N:
        if sum_of_digits == S:
            return 1
        return 0
    
    cnt = 0
    for i in range(10):
        cnt += count_pins(depth + 1, N, sum_of_digits + i, S)
    return cnt

while True:
    line = input().rstrip()
    if line == "":
        break

    n, s = map(int, line.split())
    print(count_pins(0, n, 0, s))
