input = open(0).readline
N, M = map(int, input().rstrip().split(":"))


if N < M:
    A, B = M, N # 항상 A가 더 크도록
else:
    A, B = N, M

# GCD 구하기
while B > 0:
    A, B = B, A % B
# A가 최대공약수(gcd)

print(f"{N//A}:{M//A}")
