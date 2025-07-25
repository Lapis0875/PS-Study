from sys import stdin, setrecursionlimit
from typing import Final

setrecursionlimit(10 ** 5)

class Node:
    """노드 객체"""
    children: list["Node"]
    idx: int
    __slots__ = ("children", "idx")
    
    def __init__(self, idx: int):
        self.idx = idx
        self.children = []
    
    def connect(self, other: "Node"):
        self.children.append(other)
    
    def is_leaf(self) -> bool:
        return len(self.children) == 0
    
    def is_connected(self, other: "Node") -> bool:
        return other in self.children

    def __hash__(self) -> int:
        return hash(self.idx + hash(self.children))

N: Final[int]
R: Final[int]
Q: Final[int]
N, R, Q = map(int, stdin.readline().split())
node_counts: list[int] = [1 for _ in range(N + 1)]      # 1~N의 노드 별 서브트리 노드 개수를 세어둔다.
nodes: list[Node] = [Node(i) for i in range(N + 1)]     # 1~N의 노드를 생성한다. 0번 노드는 사용하지 않는다.

for _ in range(N-1):
    u, v = map(int, stdin.readline().split())
    nodes[u].connect(nodes[v])
    nodes[v].connect(nodes[u])

def count_subtree_nodes(node: Node, parent: int) -> int:
    for child_node in node.children:
        if child_node.idx != parent:
            node_counts[node.idx] += count_subtree_nodes(child_node, node.idx)
    return node_counts[node.idx]

count_subtree_nodes(nodes[R], R)

for _ in range(Q):
    idx: int = int(stdin.readline())
    print(node_counts[idx])
