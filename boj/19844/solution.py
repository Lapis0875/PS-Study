input = open(0).readline
text = input().strip()
front = ("c", "j", "n", "m", "t", "s", "l", "d", "qu")
back = ("a", "e", "i", "o", "u", "h")

words = text.replace("-", " ").split()
cnt = 0
for w in words:
    if "'" in w:
        f, b = w.split("'", 1)
        if f in front and b[0] in back:
            cnt += 2
        else:
            cnt += 1
    else:
        cnt += 1
print(cnt)