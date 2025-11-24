input = open(0).readline

def get_group_len(part):
    return part[1] - part[0]

def dfs(string_groups):
    """
    Backtracking (DFS with condition) using string's group information.
    
    Arguments:
        string_groups (list[tuple[int, int]]): list of group info(tuple of two integers: start & end index)
    """
    if len(string_groups) == 1: # end of dfs
        res = string_groups[0][1] - string_groups[0][0] >= 2 # return whether we can remove last part.
        return res
    
    res = False
    # Case 1. Remove first elem
    if get_group_len(string_groups[0]) >= 2:
        res = dfs([*string_groups[1:]])
    # Case 2. Remove middle elem
    for gruop_idx in range(1, len(string_groups) - 1):
        diff = get_group_len(string_groups[gruop_idx])
        if diff < 2:
            continue
        left = [*string_groups[:gruop_idx - 1]]
        mid = (string_groups[gruop_idx - 1][0], string_groups[gruop_idx + 1][1] - diff)
        left.append(mid)
        if gruop_idx < len(string_groups) - 2:
            left.extend(map(lambda p: (p[0] - diff, p[1] - diff), string_groups[gruop_idx+2:]))
        res = dfs(left)
        if res:
            break
    # Case 3. Remove last elem
    if not res and get_group_len(string_groups[-1]) >= 2:
        res = dfs([*string_groups[:-1]])
    return res

for _ in range(int(input())):
    orig_group = input().strip()
    groups = []
    prev = orig_group[0]
    prev_start = 0
    for idx in range(1, len(orig_group)):
        if orig_group[idx] != prev:
            groups.append((prev_start, idx)) # [start, end)
            prev_start = idx
            prev = orig_group[idx]
    groups.append((prev_start, len(orig_group))) # last part.
    res = dfs(groups)
    print("1" if res else "0")
