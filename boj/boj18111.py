from sys import stdin
from typing import Final

FlattenData = tuple[int | float, int]       # (소요 시간, 땅의 높이), float 타입은 float("inf")를 제외하곤 허용하지 않는다.
N, M, B = map(int, stdin.readline().split())    # 세로 N, 가로 M, 인벤토리 내 기본 블럭 개수 B

maxHeight: int = -1
minHeight: int = 257
blocks: dict[int, int] = {}

for _ in range(N):
    line: list[int] = []
    for b in map(int, stdin.readline().split()):
        line.append(b)

        # 최대, 최소 높이 갱신
        if b > maxHeight:
            maxHeight = b
        if b < minHeight:
            minHeight = b

        # 개수 세기
        try:
            blocks[b] += 1
        except KeyError:
            blocks[b] = 1

print(blocks)
blocks_iter: list[tuple[int, int]] = sorted(blocks.items(), key=lambda b_c: b_c[0], reverse=True)
print(blocks_iter)
DEFAULT: Final[FlattenData] = (float("inf"), -1)

def solution(base: int, B: int) -> FlattenData:
    """
    주어진 높이 base에 맞춰 지형을 평탄화한 결과를 반환한다.
    
    Global Variables:
        world (list[list[int]]) : 2차원 배열 형식으로 표현된 집터의 땅 높이 데이터이다.     <-- (필요없어서 삭제)
        blocks (list[tuple[int, int]]) : world에 저장된 땅 높이 데이터를 Counter 객체를 활용해 개수를 센 데이터.
        N (int) : 집터의 세로 길이
        M (int) : 집터의 가로 길이

    Arguments:
        base (int) : 이 알고리즘에서, 평탄화할 기준 높이를 나타내는 정수값이다.
        B (int) : 플레이어가 현재 가지고 있는 블럭의 개수
    """
    time: int = 0

    # 일부만 캐고 일부는 채워서 더 나은 정답을 찾으려면?
    # 떠오르는 방법은 우선 world 전체 순회하면서 캐는 쪽과 채우는 쪽을 모두 해보는건데
    # world 전체를 순회하면 시간 초과가 발생한다.

    for block, count in blocks_iter:                 # 개수 순 순회하지 말고 높이 순 순회해야 한다!
        diff: int = block - base
        x: int = count * diff                        # count는 항상 양수이므로 diff에 의해 부호 결정
        print(f"block<{block},{count}> = {diff}")
        if diff > 0:
            time += 2 * x   # 이때의 diff는 양수이므로 x도 양수이다!
            B += x
        elif diff < 0:
            if B >= -x:
                time -= x    # 이때의 diff는 음수이므로 x도 음수이다!
                B += x
            else:
                return DEFAULT  # 불가능한 경우이다. 블럭을 음수로 만들면서 땅을 메울 수는 없다!
        print(f"=> time = {time}, inventory = {B}")
        if time < 0:
            return DEFAULT      # 불가능한 경우이다. 도대체 무슨 짓을 하면 시간이 0 이하가 되는거지?
    return (time, base)

res: FlattenData = DEFAULT
for block in range(minHeight, maxHeight + 1):           # 현재 집터의 땅 높이를 더 많은 값부터 순회한다. (대충 높이값 개수 많은순으로 순회)
    r = solution(block, B)
    print(f"solution( {block}, {B} ) => {r}")
    if r[0] <= res[0] and r[1] > res[1]:     # 더 적은 시간 안에, 더 높이 땅을 평탄화 할 경우, 그것을 출력해야 한다.
        res = r

print(*res)