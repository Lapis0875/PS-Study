input = open(0).readline

def gcd(a, b):
    """Greatest Common Divisor. 최대 공약수를 계산합니다. (유클리드 호제법)"""
    if a < b:
        a, b = b, a  # a가 b보다 크도록 한다.
    while b != 0:
        a, b = b, a % b
    return a

def lcm(a, b):
    """Least Common Multiple. 최소 공배수를 계산합니다."""
    return a * b // gcd(a, b)

res = []
for _ in range(int(input())):
    M, N, x, y = map(int, input().split())
    # <x:y> = k일때, 어떻게 k를 찾아야 할까?
    # 2. 굳이 1씩 늘려가며 확인해야 하는가?
    # 어짜피 x는 1~M까지 반복하므로, 원래의 x를 k로 놓고 M씩 더해가며 y의 변화를 비교해보자.
    if M == 1:
        res.append(str(y))
        continue
    elif N == 1:
        res.append(str(x))
        continue
    k = x
    while k <= lcm(M, N):
        if k % N == y or (y == N and k % N == 0):  # (k - y) mod N = 0 과 동일하다. / y가 N일때는 나머지가 0이 나오기 때문에 기존 방식으로 계산할 수 없다.
            res.append(str(k))
            break
        k += M
    else:
        res.append("-1")
print("\n".join(res))