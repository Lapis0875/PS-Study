# Migrated from ./boj/boj28113.py by boj_validator
N, A, B = map(int, input().split())
if (diff := B - A) > 0:
    print("Bus")
elif diff < 0 and N <= B:
    print("Subway")
else:
    print("Anything")