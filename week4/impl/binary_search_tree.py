from typing import Any, Generic, Optional, Protocol, TypeVar

T = TypeVar("T")

class Comparable(Protocol):
    def __eq__(self, __value: Any) -> bool:  ...
    
    def __ne__(self, __value: Any) -> bool:  ...
    
    def __lt__(self, __value: Any) -> bool:  ...
    
    def __le__(self, __value: Any) -> bool:  ...
    
    def __gt__(self, __value: Any) -> bool:  ...
    
    def __ge__(self, __value: Any) -> bool:  ...

C = TypeVar("C", bound=Comparable)

class Node(Generic[T]):
    """이진 트리의 노드 클래스. """
    
    __slots__ = ("data", "left", "right")
    
    data: T
    left: Optional["Node[T]"]
    right: Optional["Node[T]"]
    
    def __init__(self, data: T, left: Optional["Node[T]"] = None, right: Optional["Node[T]"] = None):
        self.data = data
        self.left = left
        self.right = right
    
    def isLeaf(self) -> bool:
        return self.left is None and self.right is None

    def __str__(self) -> str:
        return str(self.data)

class BinaryTree(Generic[T]):
    """이진 트리"""
    
    __slots__ = ("root", )
    
    root: Node[T]
    
    def __init__(self, root: Node[T]):
        self.root = root
    
    def preorder(self, node: Node[T]):
        print(node, end=" ")
        if node.left is not None:
            self.preorder(node.left)
        if node.right is not None:
            self.preorder(node.right)
    
    def inorder(self, node: Node[T]):
        if node.left is not None:
            self.inorder(node.left)
        print(node, end=" ")
        if node.right is not None:
            self.inorder(node.right)
    
    def postorder(self, node: Node[T]):
        if node.left is not None:
            self.postorder(node.left)
        if node.right is not None:
            self.postorder(node.right)
        print(node, end=" ")
    
class BinarySearchTree(BinaryTree, Generic[C]):
    """이진 탐색 트리"""
    
    def insert(self, key: C):
        node = Node[C](key)
        cur: Node[C] = self.root
        
        while True:
            if key > cur.data:
                if (cur.right is None):
                    cur.right = node
                    break
                else:
                    cur = cur.right
            elif key < cur.data:
                if (cur.left is None):
                    cur.left = node
                    break
                else:
                    cur = cur.left
            else:
                # BST는 키의 중복을 허용치 않으므로, 키가 동일한 경우 무시한다.
                break
                
    def search(self, key: C) -> Optional[Node[C]]:
        cur: Optional[Node[C]] = self.root
        while cur is not None:
            if key > cur.data:
                cur = cur.right
            elif key < cur.data:
                cur = cur.left
            else:
                # 동일 키의 노드 발견. 탐색 종료~
                return cur

root: int = int(input("중심 숫자 : "))
bst = BinarySearchTree[int](Node[int](root))
for i in range(1, root * 2):
    bst.insert(i)

print("\n" + "=" * 10 + "\nTree:")
bst.inorder(bst.root)
print()
while True:
    key: int = int(input("찾으려는 숫자: "))
    if key < 0:
        print("탐색을 종료합니다.")
        break
    res: Optional[Node[int]] = bst.search(key)
    if res is None:
        print(f">>> {key}는 트리에 존재하지 않습니다!")
    else:
        print(f">>> Node({res.data}, left={res.left}, right={res.right})")
