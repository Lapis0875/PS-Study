input = open(0).readline
for _ in range(int(input())):
    A, B = map(lambda s: s.strip(), input().split())
    if len(A) != len(B):
        print(f"{A} & {B} are NOT anagrams.")
        continue
    
    # First, count letters in A
    a_cnt = {}
    for c in A:
        try:
            a_cnt[c] += 1
        except KeyError:
            a_cnt[c] = 1
    
    # Second, substract letters in B.
    res = True
    for c in B:
        try:
            a_cnt[c] -= 1
            # case 1) if B has more letter than A => NOT ANAGRAM!
            if a_cnt[c] < 0:
                res = False
                break
        except KeyError:
            res = False
            break
    if not res:
        # case 2) if B has less letter than A => NOT ANAGRAM!
        for k in a_cnt:
            if a_cnt[k] != 0:
                break
    
    print(f"{A} & {B} are anagrams." if res else f"{A} & {B} are NOT anagrams.")