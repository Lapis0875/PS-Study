# Migrated from ./boj/boj1251.py by boj_validator
from sys import stdin
from queue import PriorityQueue

word: str = stdin.readline()[:-1]
length: int = len(word)
pq: PriorityQueue[str] = PriorityQueue()

for i in range(1, length - 1):  # (i, j) [0, i) [i, j) [j, length)
    for j in range(i + 1, length):
        a, b, c = word[:i], word[i:j], word[j:]
        # print(i, j, a, b, c)
        pq.put(a[::-1] + b[::-1] + c[::-1])

print(pq.get())
