input = open(0).readline
windows = [False] * 17
trace = [[] for _ in range(17)]
def simulate(n):
    # init
    for i in range(len(windows)):
        windows[i] = False
        trace[i].clear()
    # simulate
    for i in range(1, n + 1):
        for j in range(i, n + 1, i):
            windows[j] = not windows[j]
            trace[j].append(i)
    # result
    print("[Windows]")
    cnt = 0
    for i in range(1, n + 1):
        print(f"{i}: {'OPEN' if windows[i] else 'CLOSED'}")
        if windows[i]:
            cnt += 1

    print("\n[Trace]")
    for i in range(1, n + 1):
        print(f"{i}: {' '.join(map(str, trace[i]))}")
    print(f"\n[OPEN]\n{cnt}")

for i in range(1, 17):
    print("-"*6)
    print(f"N = {i}\n")
    simulate(i)
    print()
