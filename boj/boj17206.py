from sys import stdin
from typing import Final

T: Final[int] = int(stdin.readline())
arr: list[int] = list(map(int, stdin.readline().split()))
answers: dict[int, int] = {10: 25, 21: 105}

for N in arr:
    try:
        print(answers[N])
    except KeyError:
        total: int = 0
        
        # 1~K까지 합을 구하는 공식 x 3 => 3~3K까지의 합!
        # N을 3으로 나눈 몫의 3배에 해당하는 3K까지가 N 이하의 3의 배수이므로 단순 연산으로 구할 수 있다.
        a: int = N // 3
        total += (a * (a + 1) // 2) * 3
        
        b: int = N // 7
        total += (b * (b + 1) // 2) * 7
        
        c: int = N // 21
        total -= (c * (c + 1) // 2) * 21
        print(total)
        answers[N] = total
