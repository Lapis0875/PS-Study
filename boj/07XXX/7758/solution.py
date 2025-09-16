input = open(0).readline
N = int(input())
office = {}
for _ in range(N):
    name, status = input().rstrip().split()
    if status == "enter":
        office[name] = True
    else:
        try:
            office.pop(name)
        except KeyError:
            pass

names = sorted(office.keys(), reverse=True)
for name in names:
    print(name)