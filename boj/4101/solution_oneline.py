# Migrated from ./boj/boj4101_oneline.py by boj_validator
while (line := input()) != "0 0": (nums := [int(v) for v in line.split(" ")], print("Yes" if nums[0] > nums[1] else "No"))