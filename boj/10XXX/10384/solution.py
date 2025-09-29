input = open(0).readline

def solve(text):
    counter = [0] * 26 # A ~ Z
    for ch in text:
        if ch.isalpha():
            ch = ch.upper()
            idx = ord(ch) - ord('A')
            counter[idx] += 1
    pangram_cnt = min(counter)
    if pangram_cnt == 0:
        return "Not a pangram"
    elif pangram_cnt == 1:
        return "Pangram!"
    elif pangram_cnt == 2:
        return "Double pangram!!"
    else:
        return "Triple pangram!!!"

for i in range(1, int(input()) + 1):
    text = input().rstrip()
    print(f"Case {i}: {solve(text)}")