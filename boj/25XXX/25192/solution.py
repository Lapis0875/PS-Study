input = open(0).readline
N = int(input())
greetings = {}

bears = 0
for _ in range(N):
    name = input().rstrip()
    if name == "ENTER":
        greetings.clear()
    else:
        if not greetings.get(name, False):
            greetings[name] = True
            bears += 1
print(bears)
