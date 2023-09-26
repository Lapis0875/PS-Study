from sys import stdin
from contextlib import suppress

text: list[str] = []
width: int = 0
for _ in range(5):
    line: str = stdin.readline()[:-1]
    text.append(line)
    if (l := len(line)) > width:
        width = l

for i in range(width):
    for j in range(5):
        with suppress(IndexError):
            c = text[j][i]
            if not c == "":
                print(c, end="")
print()