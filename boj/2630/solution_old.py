# Migrated from ./boj/boj2630.py by boj_validator
from sys import stdin

N = int(stdin.readline())

paper: list[list[bool]] = []

for _ in range(N):
    row: list[bool] = []
    line: str = stdin.readline()[:-1]
    for tile in line:
        row.append(tile == "1")
    
    paper.append(row)

white: int = 0
blue: int = 0

for y in range(N // 2):
    for x in range(N // 2):
        blue_in_2by2: int = 0
        if paper[y][x]:
            print(f"({x}, {y}), ({x+1}, {y+1})")
            blue_in_2by2 += 1
        if paper[y][x + 1]:
            print(f"({x}, {y}), ({x-1}, {y+1})")
            blue_in_2by2 += 1
        white += 2 - blue_in_2by2
        blue += blue_in_2by2

print(blue)
print(white)
