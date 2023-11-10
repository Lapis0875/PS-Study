from sys import maxsize, stdin

N: int = int(stdin.readline())
length: int = 2 * N
students: list[int] = sorted(map(int, stdin.readline().split()))

answer: int = maxsize
for i in range(N):
    w: int = students[i] + students[length-1-i]
    if w < answer:
        answer = w

print(answer)