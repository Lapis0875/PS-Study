from typing import Final
from sys import maxsize

type index = int
type number = int | float
type edge = tuple[int, int]
type set_of_edges = set[edge]

Infinity: Final[number] = maxsize

def dijkstra(n: int, W: list[list[number]], F: set_of_edges):    
    touch: list[index] = [0 for _ in range(n + 1)]      # 2~n번 인덱스를 사용하기 위해, n+1 길이의 리스트를 만든다.
    length: list[number] = [0 for _ in range(n + 1)]    # 2~n번 인덱스를 사용하기 위해, n+1 길이의 리스트를 만든다.
    
    for i in range(2, n+1):
        touch[i] = 1
        length[i] = W[1][i]
    
    for loop in range(n - 1):      # repeat n-1 times
        minimum = Infinity
        vnear: index = 0
        for i in range(2, n + 1):
            if 0 <= length[i] < minimum:
                minimum = length[i]
                vnear: index = i
        
        e: edge = (touch[vnear], vnear)
        F.add(e)
        
        for i in range(2, n + 1):
            if length[vnear] + W[vnear][i] < length[i]:
                length[i] = length[vnear] + W[vnear][i]
                touch[i] = vnear
        
        length[vnear] = -1
        
        # F를 출력한다.
        print(f"loop {loop + 1}")
        for e in F:
            u, v = e
            print(f"{u} -> {v}")
        print()

N: Final[int] = 5
W: list[list[number]] = [
    [0, 0, 0, 0, 0, 0],
    [0, 0, 7, 4, 6, 1],
    [0, Infinity, 0, Infinity, Infinity, Infinity],
    [0, Infinity, 2, 0, 5, Infinity],
    [0, Infinity, 3, Infinity, 0, Infinity],
    [0, Infinity, Infinity, Infinity, 1, 0]
]
F: set_of_edges = set()

dijkstra(N, W, F)
print("최종 F")
for u, v in F:
    print(f"{u} -> {v}")
