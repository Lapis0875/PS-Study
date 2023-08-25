from sys import stdin
from typing import Final
from datetime import datetime

WOD: Final[list[str]] = ["MON", "TUE", "WED", "THU", "FRI", "SAT", "SUN"]

m, d = map(int, stdin.readline().split())
dt: datetime = datetime(2007, m, d)
print(WOD[dt.weekday()]) 