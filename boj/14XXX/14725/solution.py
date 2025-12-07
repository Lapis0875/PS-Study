class Node:
    """Trie의 노드 클래스."""
    def __init__(self, value):
        self.value = value
        self.children = {}
    
    def add_child(self, value):
        try:
            return self.children[value]
        except KeyError:
            self.children[value] = Node(value)
            return self.children[value]
    
    def get_child(self, value):
        return self.children.get(value)

# Trie 구조를 출력하는 함수
def print_node(node, depth=0):
    print(f"{'--'*depth}{node.value}")
    
    for child in sorted(node.children.keys()):
        print_node(node.children[child], depth + 1)

def print_trie(root):
    for child in sorted(root.children.keys()):
        print_node(root.children[child], 0)
    
root = Node(None)

input = open(0).readline

for _ in range(int(input())):
    line = input().rstrip().split()
    K = int(line[0])

    # Trie 구성하기
    cur = root
    for word in line[1:]:
        cur = cur.add_child(word)

# Trie 구조 출력하기
print_trie(root)
