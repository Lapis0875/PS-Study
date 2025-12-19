input = open(0).readline

# 아이디어
# 전화번호의 한 자리씩 Trie의 노드로 만들고 연결한 뒤
# 모든 전화번호를 등록한 뒤 Trie의 루트부터 탐색하며
# 마지막 노드가 아닌데 value를 가지는 노드가 있는지 확인한다
# 있다면 잘못된 전화번호부

class TrieNode:
    """Trie를 구성하는 노드 구현"""
    def __init__(self, key, value = None):
        self.key = key
        self.value = value
        self.children = {}
    
    @property
    def is_end(self):
        return len(self.children) == 0

    def add_child(self, key_idx, value = None):
        key_str = value[key_idx]
        child = self.children.get(key_str, None)
        if child is None:
            child = TrieNode(key_str, None)
            self.children[key_str] = child
        
        if key_idx == len(value) - 1:
            child.value = value
        else:
            child.add_child(key_idx + 1, value)

def check_trie(node):
    """"주어진 Trie에 끝단 노드가 아닌데 값을 가지는 노드가 있는지를 검사한다."""
    if node.is_end:
        return True
    
    res = True
    for child in node.children.values():
        if child.value is not None and not child.is_end:
            return False
        else:
            res = res and check_trie(child)
    return res

root = TrieNode(None)
for _ in range(int(input())):
    root.children.clear()
    N = int(input())
    for _ in range(N):
        root.add_child(0, input().rstrip())
    
    print("YES" if check_trie(root) else "NO")