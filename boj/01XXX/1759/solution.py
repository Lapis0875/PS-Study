input = open(0).readline
L, C = map(int, input().split())
alphabets = input().rstrip().split()
alphabets.sort()
alphabets_used = [False] * C
cypher = [""] * L
vowels_cnt = 0
consonants_cnt = 0
vowels = {"a": True, "e": True, "i": True, "o": True, "u": True}

def backtracking(depth, start):
    global vowels_cnt, consonants_cnt
    if depth == L:
        if vowels_cnt >= 1 and consonants_cnt >= 2:
            print("".join(cypher))
        return
    
    for alpha in range(start, C):
        if not alphabets_used[alpha]:
            cypher[depth] = alphabets[alpha]
            alphabets_used[alpha] = True
            if vowels.get(alphabets[alpha], False):
                vowels_cnt += 1
            else:
                consonants_cnt += 1

            backtracking(depth + 1, alpha + 1)

            alphabets_used[alpha] = False
            if vowels.get(alphabets[alpha], False):
                vowels_cnt -= 1
            else:
                consonants_cnt -= 1
    cypher[depth] = ""

backtracking(0, 0)
