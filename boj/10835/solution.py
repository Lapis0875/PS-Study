input = open(0).readline
N = int(input())
A = tuple(map(int, input().split()))
B = tuple(map(int, input().split()))

def top_down():
    """
    TOP DOWN 접근 - dfs + memoization
    DP배열의 구성
    0차원(결과값): 현재 경우의 점수 (-1일시 계산되지 않은 항목임.)
    1차원(카드): A 카드의 버린 장 수
    2차원(카드): B 카드의 버린 장 수
    """
    DP = [[0 for _ in range(N + 1)] for _ in range(N + 1)]
    for l in range(1, N + 1):
        for r in range(1, N + 1):
            if A[l] > B[r]:
                DP[l][r] = DP[l][r-1] + B[r]
            else:
                DP[l][r] = max(DP[l-1][r], DP[l-1][r-1])
    print(DP(0, 0))

def bottom_up():
    """
    BOTTOM UP 접근 - dp로 깡그리 구성 (아니 어떻게 점화식 생각해요???)
    DP배열의 구성
    0차원(결과값): 현재 경우의 점수
    1차원(카드): A 카드의 남은 장 수
    2차원(카드): B 카드의 남은 장 수
    """
    DP = [[0 for _ in range(N + 1)] for _ in range(N + 1)]
    for l in range(N - 1, -1, -1):
        for r in range(N - 1, -1, -1):
            if A[l] > B[r]:
                DP[l][r] = DP[l][r+1] + B[r]
            else:
                DP[l][r] = max(DP[l+1][r+1], DP[l+1][r])
    print(DP[0][0])

bottom_up()