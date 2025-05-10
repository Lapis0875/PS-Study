# Migrated from ./boj/boj1308.py by boj_validator
from sys import stdin
from datetime import datetime, timedelta

Y1, M1, D1 = map(int, stdin.readline().split())
Y2, M2, D2 = map(int, stdin.readline().split())

today: datetime = datetime(Y1, M1, D1)
yeardiff: int = Y2 - Y1
if (yeardiff > 1000 or (yeardiff == 1000 and (M2 > M1 or (M2 == M1 and D2 >= D1)))):
    print("gg")
else:
    dday: datetime = datetime(Y2, M2, D2)
    td: timedelta = dday - today
    print(f"D-{td.days}")
