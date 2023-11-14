from typing import Final

N: Final[int] = 4

keys: list[str] = ["Don", "Isabelle", "Ralph", "Wally"]
R: list[list[int]] = [
    [0, 0, 0, 0, 0],
    [0, 1, 1, 2, 2],
    [0, 0, 2, 2, 2],
    [0, 0, 0, 3, 3],
    [0, 0, 0, 0, 4],
    [0, 0, 0, 0, 0]
]

class Node[T]:
    """트리에 사용되는 노드 객체"""
    def __init__(self, key: T):
        self.key: T = key
        self.left: Node[T] | None = None
        self.right: Node[T] | None = None
    
    def is_leaf(self) -> bool:
        """이 노드가 말단 노드인지 검사한다.

        Returns:
            bool: 이 노드가 말단 노드이면 True, 그렇지 않으면 False
        """
        return self.left is None and self.right is None

def tree(i: int, j: int, R: list[list[int]], keys: list[str]) -> Node[str] | None:
    p: Node[str] | None = None
    k: int = R[i][j]
    if k == 0:
        return None
    else:
        p = Node(keys[k-1])
        p.left = tree(i, k-1, R, keys)
        p.right = tree(k+1, j, R, keys)
        return p

def max_key_len[T](keys: list[T]) -> int:
    return max(map(lambda k: len(str(k)), keys))

def fix_width[T](node: Node[T] | None, max_width: int, depth: int) -> str:
    text = f"{" " * (max_width + 2)}" if node is None else f"({str(node.key).center(max_width)})"
    if depth > 0:
        linewidth: int = (max_width + 2) * 2 ** (depth) + 2 ** depth - 1
        text = text.center(linewidth)
    return text

def print_tree[T](root: Node[T], keys: list[T]):
    """
    이진 트리를 출력한다.

    Args:
        root (Node[T]): 출력할 이진 트리의 루트 노드
    """
    if root is None:
        return
    max_str_width: Final[int] = max_key_len(keys)
    
    node_per_depth: list[list[Node[T] | None]] = [[root]]
    depth: int = 0
    
    while True:
        cur_nodes: list[Node[T] | None] = node_per_depth[depth]
        next_nodes: list[Node[T] | None] = []
        for node in cur_nodes:
            next_nodes.append(node.left if node is not None else None)
            next_nodes.append(node.right if node is not None else None)
        if all(map(lambda node: node is None, next_nodes)):
            break
        node_per_depth.append(next_nodes)
        depth += 1
    
    tree_str: list[str] = []
    tree_str.append(" ".join(map(lambda node: fix_width(node, max_str_width, 0), node_per_depth.pop(-1))))     # 말단 노드 행 처리
    
    for i, cur_nodes in enumerate(node_per_depth[::-1], 1):
        cur_str: str = " ".join(map(lambda node: fix_width(node, max_str_width, i), cur_nodes))
        tree_str.append(cur_str)
    for line in tree_str[::-1]:
        print(line)

if __name__ == "__main__":
    # root: Node[str] | None = tree(1, N)
    root = Node[str]("Hello")
    root.left = Node[str]("World")
    root.right = Node[str]("ouo!")
    root.left.left = Node[str]("I'm")
    root.left.right = Node[str]("Very")
    root.right.left = Node[str]("Happy")
    root.right.right = Node[str]("Today")
    newRoot = Node[str]("HaHaH")
    newRoot.left = Node[str]("Tex")
    newRoot.left.right = Node[str]("Latex")
    newRoot.left.right.left = Node[str]("Tux")
    newRoot.right = root
    print_tree(newRoot, ["Hello", "World", "ouo!", "I'm", "Very", "Happy", "Today", "HaHaH", "Tex", "Latex", "Tux"])
