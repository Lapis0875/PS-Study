from math import ceil, log2
input = open(0).readline
N, M = map(int, input().split())
tree_height = ceil(log2(N))
tree_size = 1 << (tree_height + 1)
arr = [0] * N
tree = [0] * tree_size

def build_segment_tree(node, start, end):
    if start == end:
        tree[node] = arr[start]
    else:
        mid = (start + end) // 2
        build_segment_tree(node * 2, start, mid)
        build_segment_tree(node * 2 + 1, mid + 1, end)
        tree[node] = tree[node * 2] + tree[node * 2 + 1]

build_segment_tree(1, 0, N - 1)

def query(node, start, end, left, right):
    """세그먼트 트리에서 (left, right) 구간에 해당하는 구간 합을 구한다.
    node: 현재 노드의 번호 (실제 tree 배열에 저장된 위치)
    start, end: 현재 노드에 저장된 구간 정보
    left, right: 찾고자 하는 구간 정보
    """
    if left > end or right < start: # 찾는 구간이 이 노드에 아예 포함되지 않는 경우
        return 0
    elif left <= start and right >= end: # 찾는 구간이 이 노드에 완전히 포함되는 경우
        return tree[node]
    else:
        mid = (start + end) // 2
        lsum = query(node * 2, start, mid, left, right)
        rsum = query(node * 2 + 1, mid + 1, end, left, right)
        return lsum + rsum

def update_tree(node, start, end, index, diff):
    """배열의 index번째 원소를 변경한다. 구간 합 정보를 트리 전체에 갱신해준다.
    node: 현재 노드의 번호 (실제 tree 배열에 저장된 위치)
    start, end: 현재 노드에 저장된 구간 정보
    index: 갱신된 배열 원소의 위치
    diff: 기존 값과 갱신된 값의 차.
    """
    if index < start or index > end: # 갱신된 원소가 이 구간에 포함되지 않는다.
        return
    tree[node] += diff
    if start != end: # leaf 노드가 아니라면
        mid = (start + end) // 2
        update_tree(node * 2, start, mid, index, diff)
        update_tree(node * 2 + 1, mid + 1, end, index, diff)

def update(index, val):
    """배열의 index번째 원소를 val로 변경한다."""
    diff = val - arr[index]
    arr[index] = val
    update_tree(1, 0, N - 1, index, diff)

for _ in range(M):
    cmd, i, j = map(int, input().split())
    if cmd == 0:
        if i > j:
            i, j = j, i
        print(query(1, 0, N - 1, i - 1, j - 1))
    else:
        update(i - 1, j)