from math import ceil, log2

MOD = 1_000_000_007
input = open(0).readline
N, M, K = map(int, input().split())

tree_height = ceil(log2(N))
tree_size = 1 << (tree_height + 1)
arr = list(int(input()) for _ in range(N))
tree = [0] * tree_size

def build_segment_tree(node, start, end):
    """세그먼트 트리를 초기화한다."""
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
    if start > right or end < left: # 찾고자 하는 구간에 현재 구간이 완전히 포함되지 않는 경우
        return 1
    elif start >= left and end <= right: # 찾고자 하는 구간에 현재 구간이 완전히 포함될 경우
        return tree[node]
    else: # 찾고자 하는 구간에 현재 구간의 일부만 포함될 경우
        mid = (start + end) // 2
        lmul = query(node * 2, start, mid, left, right)
        rmul = query(node * 2 + 1, mid + 1, end, left, right)
        return (lmul * rmul) % MOD

def update(node, start, end, index, val):
    """기존 배열에서 index 위치에 저장된 값을 val로 수정한다.
    이후 세그먼트 트리에 저장된 구간 곱을 갱신한다.
    node: 현재 노드의 번호 (tree에 저장된 위치)
    start, end: 현재 노드에 저장된 구간
    index, val: 기존 배열에서 값이 변한 위치와 그 값
    """
    if start > index or end < index: # 현재 구간에 index를 포함되지 않는 경우.
        return
    elif start == end: # 현재 노드가 leaf일 경우.
        tree[node] = val
        arr[index] = val
    else: # 현재 구간에 index가 포함되는 경우
        mid = (start + end) // 2
        update(node * 2, start, mid, index, val)
        update(node * 2 + 1, mid + 1, end, index, val)
        tree[node] = (tree[node * 2] * tree[node * 2 + 1]) % MOD
    

for _ in range(M + K):
    a, b, c = map(int, input().split())
    if a == 1:
        update(1, 0, N - 1, b - 1, c)      # 실제 인덱스는 0...N-1이므로 1씩 빼서 사용.
    else:
        print(query(1, 0, N - 1, b - 1, c - 1)) # 실제 인덱스는 0...N-1이므로 1씩 빼서 사용.
