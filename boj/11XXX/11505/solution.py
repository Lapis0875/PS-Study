from math import ceil, log2

MOD = 1_000_000_007
input = open(0).readline
N, M, K = map(int, input().split())

tree_height = ceil(log2(N))
tree_size = 1 << (tree_height + 1)
arr = list(int(input()) for _ in range(N))
tree = [0] * tree_size

def build_segment_tree(node, start, end):
    """세그먼트 트리 배열을 초기화합니다."""
    if start == end:
        tree[node] = arr[start]
    else:
        mid = (start + end) // 2
        build_segment_tree(node * 2, start, mid)
        build_segment_tree(node * 2 + 1, mid + 1, end)
        tree[node] = (tree[node * 2] * tree[node * 2 + 1]) % MOD

build_segment_tree(1, 0, N - 1)

def query(node, start, end, left, right):
    """세그먼트 트리에서 (left, right) 구간에 해당하는 곱을 구한다.
    node: 현재 노드의 번호 (tree에 저장된 위치)
    start, end: 현재 노드에 저장된 구간
    left, right: 찾고자 하는 구간
    """
    # print(f"query({left}, {right}) in tree[{node}] ({start}, {end})")
    if start > right or end < left: # 현재 노드는 찾고자 하는 구간에 완전히 포함되지 않음
        # print(f"=> 1 (포함되지 않음)")
        return 1
    elif start >= left and end <= right:
        # print(f"=> tree[node] = {tree[node]} (완전히 포함됨)")
        return tree[node]
    else:
        # print(f"=> 부분적으로 포함됨")
        mid = (start + end) // 2
        lmul = query(node * 2, start, mid, left, right)
        rmul = query(node * 2 + 1, mid + 1, end, left, right)
        res = (lmul * rmul) % MOD
        # print(f"=> tree[{node}] ({start}, {end}) 에서 ({left, right})에 포함되는 구간 곱 -> {res}")
        return (lmul * rmul) % MOD

def update_tree(node, start, end, index, val):
    if start > index or end < index:
        return
    elif start == end:
        tree[node] = val
        arr[index] = val
    else:
        mid = (start + end) // 2
        update_tree(node * 2, start, mid, index, val)
        update_tree(node * 2 + 1, mid + 1, end, index, val)
        tree[node] = (tree[node * 2] * tree[node * 2 + 1]) % MOD
    
def update(index, val):
    arr[index] = val
    update_tree(1, 0, N - 1, index, val)

for _ in range(M + K):
    a, b, c = map(int, input().split())
    if a == 1:
        update(b - 1, c)
    else:
        print(query(1, 0, N - 1, b - 1, c - 1))
