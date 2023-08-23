word: str = input()
l: int = len(word)
for i in range(l // 2):
    if word[i] != word[l - 1 - i]:
        print(0)
        break
else:
    print(1)
