MOD = 1_000_000_007
input = open(0).readline

def mod_pow(base, exp):
    # base %= MOD # base는 항상 MOD보다 작은 수로 주어지므로 불필요하다.
    ans = 1
    while exp > 0: # 지수를 2진수로 나타냈을 때의 각 자릿수를 낮은 비트부터 보며 반복한다.
        if exp & 1: # 현재 비트가 1이면, 현재의 거듭제곱 값을 결과값에 곱해준다.
            ans = ans * base % MOD
        base = base * base % MOD # 다음 비트 자리수에 맞게 거듭제곱을 진행한다.
        exp >>= 1 # 다음 비트로 이동한다.
    return ans

N, M = map(int, input().split())
print((mod_pow(M, N) - mod_pow(M - 1, N)) % MOD)