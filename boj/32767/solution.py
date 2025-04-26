from sys import stdin

N, M = map(int, stdin.readline().strip().split())
S = stdin.readline().strip()

# S를 이루는 각 문자의 개수를 센다.
char_count = {}
for c in S:
    if c not in char_count:
        char_count[c] = 1
    else:
        char_count[c] += 1

# 지워야 하는 문자들을 미리 기록해 둔다.
deleted = {}
for c in sorted(char_count):
    if char_count[c] > M:
        deleted[c] = M
        break
    else:
        deleted[c] = char_count[c]
        M -= char_count[c]

# 미리 기록해 둔 정보를 토대로, 문자들을 지워서 출력한다.
for c in S:
    if c in deleted:
        if deleted[c] > 0:
            deleted[c] -= 1
        else:
            print(c, end="")
    else:
        print(c, end="")
print()
