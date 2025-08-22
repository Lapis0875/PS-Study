input = open(0).readline
print(input().strip().upper())

# logic
text = input()
to_upper = ord("a") - ord("A")
for c in text:
    print(c - to_upper, end="")