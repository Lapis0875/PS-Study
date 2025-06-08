input = open(0).readline
text = input().rstrip()

time = 0
prev = 1
for c in text:
    cur_idx = ord(c) - 64
    if prev > cur_idx:
        left = prev - cur_idx
        right = 26 - left
    else:
        right = cur_idx - prev
        left = 26 - right
    time += min(left, right)
    prev = cur_idx

print(time)