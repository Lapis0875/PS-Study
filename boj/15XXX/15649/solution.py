from sys import stdin
from typing import Final

N: Final[int]
M: Final[int]
N, M = map(int, stdin.readline().split())
arr: list[int] = [0 for _ in range(M)]              # 1 ~ M 까지 실제 수열의 값을 저장
visited: list[int] = [False for _ in range(N)]      # 1 ~ N 까지 방문 여부를 저장

def dfs(depth: int):
    if depth == M:
        print(" ".join(map(str, arr)))
        return
    
    for i in range(N):
        if not visited[i]:
            visited[i] = True
            arr[depth] = i + 1                      # 숫자는 1부터, 인덱스는 0부터.
            dfs(depth + 1)
            visited[i] = False

dfs(0)