from typing import Final

class nodetype:
    parent: int
    depth: int
    
    def __init__(self, parent: int, depth: int):
        self.parent = parent
        self.depth = depth

type universe = list["nodetype"]
N: Final[int] = 5
U: universe = [None for _ in range(N + 1)]

def makeset(index: int):
    U[index] = nodetype(index, 0)

def initial(n: int):
    global U
    U = []
    for i in range(1, n + 1):
        makeset(i)

def find(i: int) -> int:
    j: int = i
    while U[j].parent != j:
        j = U[j].parent
        
    return j

def merge(p: int, q: int):
    if p < q:
        U[q].parent = p