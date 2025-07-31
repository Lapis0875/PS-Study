from heapq import heappush, heappop
input = open(0).readline

N = int(input())
count = {}
dasom = int(input())
needed = 0

for _ in range(N - 1):
    candidate = int(input())
    try:
        count[candidate] += 1
    except KeyError:
        count[candidate] = 1

queue = []
for vote in count:
    heappush(queue, (-vote, vote))
while queue:
    _, vote = heappop(queue)
    candidates = count[vote]
    while dasom <= vote and candidates > 0:
        dasom += 1
        print(f"dasom: {dasom}")
        print(f"vote = {vote}, left candidates = {candidates}")
        needed += 1
        candidates -= 1
        count[vote] -= 1
        try:
            count[vote - 1] += 1
        except KeyError:
            count[vote - 1] = 1
        heappush(queue, (1 - vote, vote - 1))
    if dasom > vote:
        break
print(needed)