from sys import stdin
from typing import Final

N: Final[int] = int(stdin.readline())
winner_name: str = ""
winner_solve: int = 0
winner_penalty: int = 0

for _ in range(N):
    info: list[str] = stdin.readline().rstrip().split()
    name: str = info[0]
    total_penalty: int = 0
    total_solve: int = 0
    for idx in range(1, 8, 2):
        sub: int = int(info[idx])
        time: int = int(info[idx + 1])
        if time != 0:                                   # they solved this problem!
            total_solve += 1                            # solve count + 1
            total_penalty += (sub - 1) * 20 + time      # accumulate penalty time
            
    if total_solve > winner_solve or total_solve == winner_solve and total_penalty < winner_penalty:
        winner_name = name
        winner_solve = total_solve
        winner_penalty = total_penalty
    
print(winner_name, winner_solve, winner_penalty)
