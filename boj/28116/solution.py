# Migrated from ./boj/boj28116.py by boj_validator
from sys import stdin

N: int = int(stdin.readline())
arr: list[int] = []
index_arr: list[int] = [-1] * (N + 1)   # 0번 인덱스는 사용하지 않는다.
move: list[int] = [0] * (N + 1)         # 0번 인덱스는 사용하지 않는다.
for i, e in enumerate(map(int, stdin.readline().split())):
    arr.append(e)
    index_arr[e] = i

for i in range(N - 1):              # N - 1회 반복
    least: int = index_arr[i + 1]
    
    # 거리 계산
    distance: int = abs(least - i)
    move[i + 1] += distance
    move[arr[i]] += distance
    
    # 교환 결과 반영
    if distance > 0:
        index_arr[i + 1] = i
        index_arr[arr[i]] = least
        arr[i], arr[least] = arr[least], arr[i]

print(" ".join(map(str, move[1:])))