# Migrated from ./boj/boj9375.py by boj_validator
from math import comb
from sys import stdin
from typing import Final

T: Final[int] = int(stdin.readline())

class Wear:
    def __init__(self, name: str, kind: str):
        self.name = name
        self.kind = kind

for _ in range(T):
    N: Final[int] = int(stdin.readline())
    wears: dict[str, list[Wear]] = {}
    
    for _ in range(N):
        name, kind = stdin.readline().split()
        wear = Wear(name, kind)
        try:
            wears[kind].append(wear)
        except KeyError:
            wears[kind] = [wear]
    
    wear_categories: Final[int] = len(wears)
    categories: list[str] = list(wears.keys())
    
    days: int = 0
    
    for i in range(1, wear_categories + 1):
        kinds: int = comb(wear_categories, i)
        
        
