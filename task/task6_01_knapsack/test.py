from typing import Final, Literal

type index = int        # 의사 코드의 index 타입을 선언한다.

# 문제의 입력들. 배열 인덱스를 1부터 쓰기 위해 맨 앞에 0을 넣어둔다.
n: Final[int] = 4        # 물건의 개수
p: list[int] = [0, 50, 60, 70, 80]    # 물건의 가치
w: list[int] = [0, 2, 3, 7, 10]       # 물건의 무게
W: Final[int] = 15       # 배낭의 최대 용량

# 상태 변수들
# 의사코드에서 weight와 profit이라 표기된 변수들은 전역 변수들은 구현상 promising 함수에도 인자로 전달했다.
maxprofit: int = 0      # 담은 물건의 최대 가치
include: list[Literal["YES", "NO"]] = ["NO" for _ in range(n + 1)]    # 물건의 포함 여부를 기록하는 배열
numbest: int = 0        #                   # 현재 최대 가치의 경우에서 include배열을 어디까지 읽어야 하는가?
bestset: list[Literal["YES", "NO"]] = ["NO" for _ in range(n + 1)]    # 최대 가치의 경우에서의 include 배열 내용을 복사한다.

def promising(i: index, profit: int, weight: int) -> bool:
    """i번 노드가 유망한지 판단한다."""
    j: index
    k: index
    totweight: int
    bound: float
    
    if (weight >= W):       # 더 이상 물건을 담을 수 없는 경우
        return False
    else:                   # 아직 담을 수 있는 경우
        j = i + 1
        bound = profit
        totweight = weight
        while j <= n and (totweight + w[j] <= W):   # i + 1부터 n까지 담을 수 있는 만큼 담는다.
            totweight = totweight + w[j]
            bound = bound + p[j]
            j += 1
        k = j  # k부터는 담게되면 가방이 넘친다.
        if (k <= n):
            bound = bound + (W - totweight) * p[k] / w[k]   # fractional knaosack 문제를 풀어서 bound를 계산한다.
        return bound > maxprofit

def knapsack(i: index, profit: index, weight: int):
    """Backtraking을 이용하여 0-1 배낭 문제를 푼다."""
    global maxprofit, numbest, bestset  # 전역 변수의 값을 변경하기 위해 사용.
    if weight <= W and profit > maxprofit:  # 최대 가치 갱신.
        maxprofit = profit
        numbest = i
        # include 배열을 복사한다.
        for i in range(1, i+1):
            bestset[i] = include[i]
     
    if promising(i, profit, weight):            # 유망한 경우만 탐색한다.
        include[i + 1] = "YES"                  # i번 물건을 담는 경우
        knapsack(i + 1, profit + p[i + 1], weight + w[i + 1])
        include[i + 1] = "NO"                   # i번 물건을 담지 않는 경우
        knapsack(i + 1, profit, weight)

knapsack(0, 0, 0)
print(f"bestset: {bestset[1:numbest+1]}")
print(f"maxprofit: {maxprofit}")
