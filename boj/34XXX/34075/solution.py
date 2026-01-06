input = open(0).readline
N = int(input())

algorithms = {}
diff = []

for _ in range(N):
    algo_name, tier = input().split()
    try:
        algorithms[int(tier)].append(algo_name)
    except KeyError:
        algorithms[int(tier)] = [algo_name]

M = int(input())
members = {}

def get_member_algorithm(tier):
    diff.clear()
    for t, arr in algorithms.items():
        for algo in arr:
            diff.append((abs(t - tier), algo))

    diff.sort() # Python의 정렬은 이전 정렬의 상태를 유지한채 재정렬된다.
    return f"{diff[1][1]} yori mo {diff[0][1]}"

for _ in range(M):
    member_name, tier = input().split()
    tier = int(tier)
    members[member_name] = get_member_algorithm(tier)

member_name = ""
for _ in range(int(input())):
    query = input().rstrip()
    if query == "nani ga suki?":
        print(members[member_name])
    else: # "name - chan!"
        member_name = query.split()[0]
        print("hai!")
