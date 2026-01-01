a1, a0 = map(int, input().split())
c = int(input())
n0 = int(input())

print("1" if a1 * n0 + a0 <= c * n0 and c >= a1 else "0") # c >= a1인 이유는, a1이 음수인 경우에도 항상 조건이 성립하도록 하기 위함이다. 