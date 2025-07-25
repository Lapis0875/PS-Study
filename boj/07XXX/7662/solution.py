from sys import stdin
from typing import Final
from heapq import heappush, heappop

T: Final[int] = int(stdin.readline())

class DoubleEndedPriorityQueue:
    def __init__(self):
        self.maxheap: list[int] = []
        self.max_sync: dict[int, int] = {}
        self.minheap: list[int] = []
        self.min_sync: dict[int, int] = {}
    
    def insert(self, x: int):
        heappush(self.minheap, x)
        heappush(self.maxheap, -x)
    
    @property
    def min(self) -> int | None:
        return self.minheap[0] if self.minheap else None
    
    @property
    def max(self) -> int | None:
        return -self.maxheap[0] if self.maxheap else None
    
    def delete_min(self):
        while self.minheap and self.min_sync.get(self.minheap[0], 0):
            x: int = heappop(self.minheap)
            self.min_sync[x] -= 1
            # print(f"-> Sync! 최소 힙에서 {x}를 삭제")
        if self.minheap:
            x: int = heappop(self.minheap)
            try:
                self.max_sync[-x] += 1       # 최대 힙에는 음수로 저장되니, 값 비교의 편의를 위해 음수로 기록.
            except KeyError:
                self.max_sync[-x] = 1
    
    def delete_max(self):
        while self.maxheap and self.max_sync.get(self.maxheap[0], 0):
            x: int = heappop(self.maxheap)
            self.max_sync[x] -= 1
            # print(f"-> Sync! 최대 힙에서 {x}를 삭제")
        if self.maxheap:
            x: int = heappop(self.maxheap)
            try:
                self.min_sync[-x] += 1       # 최대 힙에는 음수로 저장한 값을 최소 힙에서는 양수로 저장했으니, 다시 양수로 만든다.
            except KeyError:
                self.min_sync[-x] = 1
    
    def sync(self):
        while self.minheap and self.min_sync.get(self.minheap[0], 0):
            x: int = heappop(self.minheap)
            self.min_sync[x] -= 1
            # print(f"-> Sync! 최소 힙에서 {x}를 삭제")
        while self.maxheap and self.max_sync.get(self.maxheap[0], 0):
            x: int = heappop(self.maxheap)
            self.max_sync[x] -= 1
            # print(f"-> Sync! 최대 힙에서 {x}를 삭제")
        
    
    def debug(self, cmd: str, x: str):
        print(f">>> {cmd} {x}")
        print("최대 힙 :")
        print(self.maxheap)
        print("최대 힙에서 삭제해야하는 요소들 :")
        print(self.max_sync)
        print("최소 힙 :")
        print(self.minheap)
        print("최소 힙에서 삭제해야하는 요소들 :")
        print(self.min_sync)
        print()
    
    def __bool__(self) -> bool:
        return bool(self.minheap) and bool(self.maxheap)

for _ in range(T):
    Q: Final[int] = int(stdin.readline())
    dq = DoubleEndedPriorityQueue()
    
    for _ in range(Q):
        inst, num = stdin.readline().strip().split()
        if inst == "I":
            dq.insert(int(num))
        else:
            if num.startswith("-"):
                dq.delete_min()             # 최솟값 삭제
            else:
                dq.delete_max()             # 최댓값 삭제
        # dq.debug(inst, num)
    
    dq.sync()
    if dq:
        print(dq.max, dq.min)
    else:
        print("EMPTY")
