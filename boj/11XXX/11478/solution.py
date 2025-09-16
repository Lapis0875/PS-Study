input = open(0).readline
S = input().rstrip()
counter = {}
for s in range(len(S)):
    for e in range(s + 1, len(S) + 1):
        counter[S[s:e]] = True

print(len(counter))