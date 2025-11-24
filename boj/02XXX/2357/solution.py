from math import ceil, log2
input = open(0).readline

# Constants
N, M = map(int, input().split())
tree_height = ceil(log2(N))
tree_size = 1 << (tree_height + 1)
NUMBER_MAX = 1_000_000_001
NUMBER_MIN = 0

# Original Data
arr = list(int(input()) for _ in range(N))

# Segment Tree Impl
class QueryParam:
    """재귀 호출의 중복 인수를 제거하기 위한 데이터 객체"""
    __slots__ = ("left", "right")
    NONE = 0
    ALL = 1
    PARTIAL = 2
    def __init__(self):
        self.left = 0
        self.right = N - 1

    def set(self, left, right):
        self.left = left
        self.right = right

    def check_range(self, start, end):
        if start > self.right or end < self.left: # 포함 X
            return QueryParam.NONE
        elif start >= self.left and end <= self.right: # 완전히 포함됨
            return QueryParam.ALL
        else:
            return QueryParam.PARTIAL

class CmpSegmentTree:
    """특정한 비교 조건을 통해 값을 저장하는 세그먼트 트리"""
    __slots__ = ("tree", "query_param", "cmp", "fallback_value")
    def __init__(self, cmp, fallback_value):
        self.tree = [0] * tree_size
        self.query_param = QueryParam()
        self.cmp = cmp
        self.fallback_value = fallback_value

    def init(self, node, start, end):
        if start == end:
            self.tree[node] = arr[start]
        else:
            mid = (start + end) // 2
            self.init(node * 2, start, mid)
            self.init(node * 2 + 1, mid + 1, end)
            self.tree[node] = self.cmp(self.tree[node * 2], self.tree[node * 2 + 1])
    
    def _query_tree(self, node, start, end):
        check = self.query_param.check_range(start, end)
        if check == QueryParam.NONE: # 범위 밖 (포함 X)
            return self.fallback_value
        elif check == QueryParam.ALL: # 범위 안에 완전히 포함됨.
            return self.tree[node]
        else:
            mid = (start + end) // 2
            left_res = self._query_tree(node * 2, start, mid)
            right_res = self._query_tree(node * 2 + 1, mid + 1, end)
            return self.cmp(left_res, right_res)
    
    def query(self, left, right):
        self.query_param.set(left, right)
        return self._query_tree(1, 0, N - 1)

max_segment_tree = CmpSegmentTree(max, NUMBER_MIN)
min_segment_tree = CmpSegmentTree(min, NUMBER_MAX)
max_segment_tree.init(1, 0, N - 1)
min_segment_tree.init(1, 0, N - 1)

for _ in range(M):
    a, b = map(lambda v: int(v) - 1, input().split())
    if a > b:
        a, b = b, a
    print(min_segment_tree.query(a, b), max_segment_tree.query(a, b))