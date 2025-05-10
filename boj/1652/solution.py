# Migrated from ./boj/boj1652.py by boj_validator
from sys import stdin

N: int = int(stdin.readline())
room: list[list[bool]] = []
for _ in range(N):
    line: list[bool] = []
    for c in stdin.readline()[:-1]:
        line.append(c == '.')
    room.append(line)

horizontal: int = 0
vertical: int = 0

for i in range(N):
    j: int = 0
    horiznotal_count: int = 0
    vertical_count: int = 0
    while j <= N - 1:
        tile: bool = room[i][j]
        
        horiznotal_count += tile
        if not tile:
            if horiznotal_count >= 2:
                horizontal += 1
            horiznotal_count = 0
        
        tile: bool = room[j][i]
        
        vertical_count += tile
        if not tile :
            if vertical_count >= 2:
                vertical += 1
            vertical_count = 0
        
        j += 1
            
    horizontal += (horiznotal_count >= 2)
    vertical += (vertical_count >= 2)

print(horizontal, vertical)
