text: str = input()
length: int = 10

for i in range(1, len(text)):
    length += 10 if text[i-1] != text[i] else 5

print(length)