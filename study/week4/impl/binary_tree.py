from typing import Generic, Optional, TypeVar
from queue import LifoQueue

T = TypeVar("T")

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

def buildBinaryTree() -> BinaryTree:
    """
    Build Binary Tree below:
    
             5
           /   \\
          4     7
         /\\   / \\
        1   2 6   8
                   \\
                   10
    
    Returns:
        BinaryTree: BinaryTree instance.
    """
    root = Node[int](5)
    root.left = Node[int](4)
    root.right = Node[int](7)
    root.left.right = Node[int](2)
    root.left.left = Node[int](1)
    root.right.left = Node[int](6)
    root.right.right = Node[int](8)
    root.right.right.right = Node[int](10)
    return BinaryTree(root)

btree = buildBinaryTree()
print("=" * 10 + "\nPreorder:")
btree.preorder(btree.root)
print("\n" + "=" * 10 + "\nInorder:")
btree.inorder(btree.root)
print("\n" + "=" * 10 + "\nPostorder:")
btree.postorder(btree.root)
print()