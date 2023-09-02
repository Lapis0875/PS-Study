from sys import stdin
from typing import Final

N: Final[int] = int(stdin.readline())
Flowers: list[int] = list(map(int, stdin.readline().split()))

totalP: int = 0

def calculate_p(flowers: list[int]) -> int:
    P: int = 1
    for flower in flowers:
        P *= flower
    return P

tp = calculate_p(Flowers[:-3]) + calculate_p(Flowers[-3:-2]) + calculate_p(Flowers[-2:-1]) + calculate_p(Flowers[-1:])
# 현재의 P 합이 더 큰 경우, 이를 기록한다.
if tp > totalP:
    totalP = tp
    
tp = calculate_p(Flowers[:1]) + calculate_p(Flowers[1:-2]) + calculate_p(Flowers[-2:-1]) + calculate_p(Flowers[-1:])
# 현재의 P 합이 더 큰 경우, 이를 기록한다.
if tp > totalP:
    totalP = tp
    
tp = calculate_p(Flowers[:1]) + calculate_p(Flowers[1:2]) + calculate_p(Flowers[2:-1]) + calculate_p(Flowers[-1:])
# 현재의 P 합이 더 큰 경우, 이를 기록한다.
if tp > totalP:
    totalP = tp
    
tp = calculate_p(Flowers[:1]) + calculate_p(Flowers[1:2]) + calculate_p(Flowers[2:3]) + calculate_p(Flowers[3:])
# 현재의 P 합이 더 큰 경우, 이를 기록한다.
if tp > totalP:
    totalP = tp

print(totalP)