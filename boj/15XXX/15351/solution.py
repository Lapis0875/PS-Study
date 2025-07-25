input = open(0).readline
for _ in range(int(input().strip())):
    content = input().strip()
    score = 0
    for c in content:
        if c == " ":
            continue
        score += ord(c) - ord("A") + 1
    print("PERFECT LIFE" if score == 100 else score)