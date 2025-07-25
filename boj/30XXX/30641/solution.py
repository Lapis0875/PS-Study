input = open(0).readline
L, U = map(int, input().strip().split())
MOD = 1_000_000_007

def fast_square(x):
    """26^x mod 1,000,000,007 꼴의 계산을 square&multiply 방식으로 빠르게 계산한다.
    a^x에서, x를 2진수로 나타냈을 때 각 자리의 비트값이 1일때만 그 자리에 해당하는 지수의 거듭제곱 꼴을 곱해주는 방식이다
    ex) a^9 = a^(1001)2 = a^8 * 1 * 1 * a^1
    """
    if x == 0:
        return 1
    elif x == 1:
        return 26
    
    res = 1
    a = 26
    while x > 0:
        if x & 1 == 1:  # 지수의 LSB가 1이라면 곱한다
            res = (a * res) % MOD
        a = (a * a) % MOD # 지수를 제곱한다.
        x = x >> 1
    return res

def L2R():
    res = 0
    for i in range(L, U + 1):
        if i <= 2:
            res += 1
        else:
            res = (res % MOD + fast_square((i - 1) // 2) % MOD) % MOD
    return res

isH = (L == 1 and U == 1) or (L == 2 and U >= 2)
print("H" if isH else "A")
print(L2R())

# TODO: 모듈로 역원 찾아서 ((r-1) // 25) % MOD를 정상적으로 잘 분배해서 계산하기.

def sum(x):
    """
    S(n) = a + a*r^1 + a*r^2 + ... + a*r^{n-1} = a * (r^n - 1) / r - 1
    S(n-1) = a + ... + a*r^{n-2} = a * (r^{n-1} - 1) / r - 1
    따라서, r^{n-1}만 구해두면 된다.
    """
    if x <= 2:      # sum(1) = 1, sum(2) = 2
        return x
    
    if x % 2 == 1:
        n = (x + 1) // 2 - 1            # n - 1
        r = fast_square(n) % MOD    # 26^{n-1}
        s = ((r - 1) // 25) % MOD         # S(n-1)
        return ((2 * s) % MOD + r) % MOD
    else:
        n = (x + 1) // 2                # n
        r = fast_square(n) % MOD    # 26^{n}
        s = ((r - 1) // 25) % MOD         # S(n)
        return (2 * s) % MOD