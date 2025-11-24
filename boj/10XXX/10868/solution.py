from math import ceil, log2

input = open(0).readline
NUMBER_MAX = 1_000_000_001

N, M = map(int, input().split())
arr = list(int(input()) for _ in range(N))
tree = [0] * (1 << ceil(log2(N)) + 1)

def build_segment_tree(node, start, end):
    if start == end:
        tree[node] = arr[start]
    else:
        mid = (start + end) // 2
        build_segment_tree(node * 2, start, mid)
        build_segment_tree(node * 2 + 1, mid + 1, end)
        tree[node] = min(tree[node * 2], tree[node * 2 + 1])

def query_segment_tree(node, start, end, left, right):
    if start >= left and end <= right:
        return tree[node]
    elif start > right or end < left:
        return NUMBER_MAX
    else:
        mid = (start + end) // 2
        left_res = query_segment_tree(node * 2, start, mid, left, right)
        right_res = query_segment_tree(node * 2 + 1, mid + 1, end, left, right)
        return min(left_res, right_res)

def query(left, right):
    return query_segment_tree(1, 0, N - 1, left - 1, right - 1)

build_segment_tree(1, 0, N - 1)

for _ in range(M):
    print(query(*map(int, input().split())))