input = open(0).readline
while True:
    text = input().strip()
    if text == "#":
        break
    cnt = 0
    for c in text:
        c = c.lower()
        if c == "a" or c == "e" or c == "i" or c == "o" or c == "u":
            cnt += 1
    print(cnt)