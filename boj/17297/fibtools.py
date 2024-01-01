memo: list[int] = [5, 13]
MAX: int = 2**30-1
while memo[-1] < MAX:
    memo.append(memo[-1] + memo[-2] + 1)
print(len(memo), memo[-1], MAX, memo[-1] >= MAX)