from sys import setrecursionlimit
setrecursionlimit(10**5)

input = open(0).readline
N = int(input())
in_order = list(map(int, input().split()))
post_order = list(map(int, input().split()))

def build_tree(in_start, in_end, post_start, post_end):
    """중위 순회와 후위 순외 정보로부터 트리를 재구성해 전위 순회 결과를 출력한다.
    Arguments:
        in_start {int} -- 중위 순회의 시작 인덱스   (포함됨)
        in_end {int} -- 중위 순회의 끝 인덱스       (포함되지 않음)
        post_start {int} -- 후위 순회의 시작 인덱스 (포함됨)
        post_end {int} -- 후위 순회의 끝 인덱스     (포함되지 않음)
    """
    if post_start < post_end and in_start < in_end:
        root = post_order[post_end - 1]
        subtree_root = in_order.index(root, in_start, in_end + 1)
        print(root, end=" ") # 전위이므로 탐색 전에 출력
        # 중위 순회에서 찾은 루트 노드의 인덱스는 후위 순회에서의 루트 노드의 인덱스와 동일하지 않다. 상대적인 위치를 계산해줘야 한다.
        build_tree(in_start, subtree_root, post_start, post_start + (subtree_root - in_start))
        build_tree(subtree_root + 1, in_end, post_start + (subtree_root - in_start), post_end - 1)

build_tree(0, N, 0, N)

