input = open(0).readline

friend_count = {}
names = {}

def init_name(name):
    names[name] = name
    friend_count[name] = 1

def find_root(name):
    # print(f"find_root({name})")
    path = []
    while name != names[name]:
        # print(f"- {name}")
        path.append(name)
        name = names[name]
    # print(f"=> {name}")
    for p in path:
        names[p] = name
    
    return name

def union(a, b):
    # print(f"union({a}, {b})")
    a_root = find_root(a)
    b_root = find_root(b)

    if a_root == b_root:
        return False

    names[b_root] = a_root
    friend_count[a_root] += friend_count[b_root]
    return True

for _ in range(int(input())):
    N = int(input())
    names.clear()
    friend_count.clear()
    for _ in range(N):
        name1, name2 = input().rstrip().split()

        # 초기화
        if names.get(name1, None) is None:
            init_name(name1)
        if names.get(name2, None) is None:
            init_name(name2)
        
        # 병합
        union(name1, name2)
        print(friend_count[find_root(name1)])