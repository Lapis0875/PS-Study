# Migrated from ./boj/boj28117.py by boj_validator
from math import comb
from sys import stdin

N: int = int(stdin.readline())
text: str = stdin.readline()[:-1]

count: int = 0      # text에서 발견된 longlong의 개수를 세어준다.
for i in range(0, N - 7):
    partition: str = text[i:i+8]
    print(partition)
    if partition == "longlong":
        count += 1

originals: int = 2      # text 그대로가 원본일 경우를 미리 세어준다.

"""
longlong:           (count = 1) => 2
longlong,           => 1C0
int                 => 1C1
 
longlonglong:       (count = 2) => 3
longlonglong,       => 2C0
intlong, longint    => 2C1

longlonglonglong:   (count = 3) => 5
longlonglonglong,                       => 3C0 x 1C1 = 1
intlonglong, longlongint, longintlong,  => 3C1 x 2C1 / 2! = 3
intint                                  => 

longlonglonglonglong:   (count = 4) => 8
longlonglonglonglong,
intlonglonglong, longintlonglong, longlongintlong, longlonglongint,
intintlong, intlongint, longintint

longlonglonglonglonglong:   (count = 5) => 13
longlonglonglonglong,                           => 5C0 x 
intlonglonglonglong, longintlonglonglong, longlongintlonglong, longlonglongintlong, longlonglonglongint,        => 5C1
intintlonglong, intlongintlong, intlonglongint, longintlongint, longintintlong, longlongintint,                 => 5C2 x 4C2 / 4! = 5
intintint
"""

for i in range(1, count + 1):
    originals += comb(count, i)

print(originals)
