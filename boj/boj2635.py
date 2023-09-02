from sys import stdin

N: int = int(stdin.readline())

nums: list[int] = []
maxLen: int = 0

for i in range(1, N + 1):
    first: int = N
    second: int = i
    v: list[int] = [first, second]
    length: int = 2
    
    while True:
        third: int = first - second
        if third < 0:
            break
        v.append(third)
        length += 1
        
        # 다음번 루프를 위한 변수 준비
        first = second
        second = third
    
    if length > maxLen:
        maxLen = length
        nums = v

print(maxLen)
print(" ".join(map(str, nums)))