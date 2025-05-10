# Migrated from ./boj/boj10811.py by boj_validator
from sys import stdin

N, M = map(int, stdin.readline().split())

arr: list[int] = list(range(N + 1))

for _ in range(M):
    i, j = map(int, stdin.readline().split())
    print(i, j)
    if i == j:                      # 2, 2 ==> 바꾸지 않고 지나간다.
        continue
    
    k: int = 0
    while k <= (j - i) // 2:        # 1, 4 ==> (1 <-> 4), (2 <-> 3) 2번만 반복하기.
        print(f"> {i + k}, {j - k}")
        arr[i+k], arr[j-k] = arr[j-k], arr[i+k]
        k += 1
    
    print(">>> " + " ".join(map(str, arr[1:])))

print(" ".join(map(str, arr[1:])))