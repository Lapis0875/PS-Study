from math import ceil, log2

input = open(0).readline
NUMBER_MAX = 1_000_000_001

N = int(input())
arr = list(map(int, input().split()))
tree = [0] * (1 << ceil(log2(N)) + 1)

def build_segment_tree(node, start, end):
    if start == end:
        tree[node] = start # 세그먼트 트리에는 인덱스 자체를 저장하기
    else:
        mid = (start + end) // 2
        build_segment_tree(node * 2, start, mid)
        build_segment_tree(node * 2 + 1, mid + 1, end)

        # 항상 구간 내 최솟값의 인덱스를 트리의 노드에 저장해준다.
        if arr[tree[node * 2]] > arr[tree[node * 2 + 1]]:
            tree[node] = tree[node * 2 + 1]
        elif arr[tree[node * 2]] < arr[tree[node * 2 + 1]]:
            tree[node] = tree[node * 2]
        else:
            tree[node] = min(tree[node * 2], tree[node * 2 + 1])

def query_segment_tree(node, start, end, left, right):
    if start >= left and end <= right:
        return tree[node]
    elif start > right or end < left:
        return N
    else:
        mid = (start + end) // 2
        left_res = query_segment_tree(node * 2, start, mid, left, right)
        right_res = query_segment_tree(node * 2 + 1, mid + 1, end, left, right)

        # 항상 구간 내 최솟값의 인덱스를 구한다.
        if left_res == N:
            if right_res == N:
                # NO!!!
                return -1
            return right_res
        elif right_res == N:
            return left_res

        if arr[left_res] > arr[right_res]:
            return right_res
        elif arr[left_res] < arr[right_res]:
            return left_res
        else: # 두 인덱스가 같은 수를 가리킬 경우, 더 작은 인덱스를 답으로 사용한다.
            return min(left_res, right_res)

def query(left, right):
    return query_segment_tree(1, 0, N - 1, left - 1, right - 1)

def update_segment_tree(node, start, end, index):
    if start == end and start == index:
        tree[node] = index
    elif start > index or end < index: # index가 포함되지 않는 구간
        return
    else:
        mid = (start + end) // 2
        update_segment_tree(node * 2, start, mid, index)
        update_segment_tree(node * 2 + 1, mid + 1, end, index)

        # 항상 구간 내 최솟값의 인덱스를 트리의 노드에 저장해준다.
        if arr[tree[node * 2]] > arr[tree[node * 2 + 1]]:
            tree[node] = tree[node * 2 + 1]
        elif arr[tree[node * 2]] < arr[tree[node * 2 + 1]]:
            tree[node] = tree[node * 2]
        else:
            tree[node] = min(tree[node * 2], tree[node * 2 + 1])

def update(index, value):
    arr[index - 1] = value
    update_segment_tree(1, 0, N - 1, index - 1)

build_segment_tree(1, 0, N - 1)

for _ in range(int(input())):
    op, *args = map(int, input().split())
    if op == 1:
        update(*args)
    else:
        print(query(*args) + 1)
    
    print("arr:")
    print(arr)
    print("tree:")
    print(tree)
    print()