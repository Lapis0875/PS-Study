# Migrated from ./boj/boj24060.py by boj_validator
from sys import stdin

N, K = map(int, stdin.readline().split())
A: list[int] = list(map(int, stdin.readline().split()))
store: int = 0

def merge_sort(start: int, end: int):
    if (start < end):
        mid: int = (start + end) // 2
        merge_sort(start, mid)
        merge_sort(mid + 1, end)
        merge(start, mid, end)

def merge(start: int, mid: int, end: int):
    global A, store
    tmp: list[int] = []
    i: int = start
    j: int = mid + 1
    while i <= mid and j <= end:
        if (A[i] < A[j]):
            tmp.append(A[i])
            i += 1
        else:
            tmp.append(A[j])
            j += 1
    tmp.extend(A[i:mid+1])
    tmp.extend(A[j:end+1])
    
    for i, v in zip(range(start, end+1), tmp):
        A[i] = v
        store += 1
        if store == K:
            print(v)
            exit(0)

merge_sort(0, N-1)
if store < K:
    print(-1)
