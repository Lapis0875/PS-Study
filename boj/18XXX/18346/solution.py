from math import ceil, log2

input = open(0).readline

N = int(input())
arr = list(map(int, input().split()))
tree_size = 1 << (ceil(log2(N)) +1)

class SegmentTree:
    """세그먼트 트리 구현체"""
    __slots__ = ("tree", "base_arr", "query_param", "update_param") # 객체를 가볍게 만들기 위해 사용 (Python3)

    def __init__(self, base_arr):
        self.tree = [0 for _ in range(tree_size)]
        self.base_arr = base_arr
        self.init(1, 0, N - 1)
        self.query_param = [0, N - 1]   # start, end
        self.update_param = [0, 0]      # idx, value
    
    def init(self, node, start, end):
        if start == end:
            self.tree[node] = self.base_arr[start]
        else:
            mid = (start + end) // 2
            self.init(node * 2, start, mid)
            self.init(node * 2 + 1, mid + 1, end)
            self.tree[node] = self.tree[node * 2] + self.tree[node * 2 + 1]
    
    def _query(self, node, start, end):
        if start > self.query_param[1] or end < self.query_param[0]: # 범위 밖 (포함 X)
            return 0
        elif start >= self.query_param[0] and end <= self.query_param[1]: # 범위 안에 완전히 포함
            return self.tree[node]
        else:
            mid = (start + end) // 2
            lsum = self._query(node * 2, start, mid)
            rsum = self._query(node * 2 + 1, mid + 1, end)
            return lsum + rsum
    
    def query(self, left, right):
        self.query_param[0] = left
        self.query_param[1] = right
        return self._query(1, 0, N - 1)

    def _update(self, node, start, end):
        if start > self.update_param[0] or end < self.update_param[0]:
            return
        elif start == end and start == self.update_param[0]:
            self.tree[node] = self.update_param[1]
        else:
            mid = (start + end) // 2
            self._update(node * 2, start, mid)
            self._update(node * 2 + 1, mid + 1, end)
            self.tree[node] = self.tree[node * 2] + self.tree[node * 2 + 1]
    
    def update(self, idx, value):
        if self.base_arr[idx] != value: # 홀수/짝수를 구분하는 배열이므로, 수가 바뀌어도 홀짝이 같다면 갱신할 필요가 없다.
            self.base_arr[idx] = value
            self.update_param[0] = idx
            self.update_param[1] = value
            self._update(1, 0, N - 1)

is_odd = [i & 1 for i in arr]
odd_tree = SegmentTree(is_odd)                      # 홀수면 1, 짝수면 0
even_tree = SegmentTree([1 - i for i in is_odd])    # 짝수면 1, 홀수면 0

for _ in range(int(input())): # 쿼리 입력
    op, i, j = map(int, input().split())
    if op == 1:     # update i x
        i -= 1
        arr[i] = j
        d = j & 1 # j가 홀수면 1, 짝수면 0
        odd_tree.update(i, d)
        even_tree.update(i, 1 - d) # d가 1이면 0, 0이면 1이 된다.

    elif op == 2:   # query(even) l r
        print(even_tree.query(i - 1, j - 1))

    else:           # query(odd) l r
        print(odd_tree.query(i - 1, j - 1))
