from datetime import datetime, timedelta
from sys import stdin
from decimal import Decimal

now_str: str = stdin.readline()[:-1]

now: datetime = datetime.strptime(now_str, "%B %d, %Y %H:%M")
year_start: datetime = datetime(now.year, 1, 1, 0, 0)
year_end: datetime = datetime(now.year + 1, 1, 1, 0, 0)

print(Decimal((now - year_start).total_seconds()) / Decimal((year_end - year_start).total_seconds()) * Decimal(100))
