input = open(0).readline

def get_part_len(part):
    return part[1] - part[0]

def dfs(s_info):
    """
    Backtracking (DFS with condition) using string's partition information.
    
    Arguments:
        s_info (list[tuple[int, int]]): list of partition info(tuple of two integers: start & end index)
    """
    if len(s_info) == 1: # end of dfs
        res = s_info[0][1] - s_info[0][0] >= 2 # return whether we can remove last part.
        return res
    
    res = False
    # Case 1. Remove first elem
    if get_part_len(s_info[0]) >= 2:
        res = dfs([*s_info[1:]])
    # Case 2. Remove middle elem
    for part_idx in range(1, len(s_info) - 1):
        diff = get_part_len(s_info[part_idx])
        if diff < 2:
            continue
        left = [*s_info[:part_idx - 1]]
        mid = (s_info[part_idx - 1][0], s_info[part_idx + 1][1] - diff)
        left.append(mid)
        if part_idx < len(s_info) - 2:
            left.extend(map(lambda p: (p[0] - diff, p[1] - diff), s_info[part_idx+2:]))
        res = dfs(left)
        if res:
            break
    # Case 3. Remove last elem
    if not res and get_part_len(s_info[-1]) >= 2:
        res = dfs([*s_info[:-1]])
    return res

for _ in range(int(input())):
    orig_group = input().strip()
    parts = []
    prev = orig_group[0]
    prev_start = 0
    for idx in range(1, len(orig_group)):
        if orig_group[idx] != prev:
            parts.append((prev_start, idx)) # [start, end)
            prev_start = idx
            prev = orig_group[idx]
    parts.append((prev_start, len(orig_group))) # last part.
    res = dfs(parts)
    print("1" if res else "0")
