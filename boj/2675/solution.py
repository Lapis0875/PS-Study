# Migrated from ./boj/boj2675.py by boj_validator
for r,_,*s,_ in [*open(0)][1:]: print("".join(c*int(r)for c in s))