from sys import stdin
from typing import Literal, cast

ANSWERS: list[Literal["A", "B", "C", "D", "E"]] = ["E", "A", "B", "C", "D"]  # 던져서 나온 윷의 배의 개수를 인덱스로 하는 정답 배열

for _ in range(3):
    res: list[Literal["0", "1"]] = cast(list[Literal["0", "1"]], stdin.readline().split())
    belly: int = 0          # 배가 나온 윷의 개수
    for c in res:
        if c == "0":
            belly += 1
    print(ANSWERS[belly])