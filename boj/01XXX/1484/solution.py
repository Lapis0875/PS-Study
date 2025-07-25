from sys import stdin

G: int = int(stdin.readline())


right: int
answer: list[int] = []
for left in range(1, G if G < 100001 else 100001):
    right = left + 1
    while right < 100001 and (d := right ** 2 - left ** 2) <= G:
        if d == G:
            answer.append(right)
        right += 1

if len(answer) > 0:
    print("\n".join(map(str, answer)))
else:
    print(-1)
