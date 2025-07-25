input = open(0).readline
N = int(input())
numbers = [0 for _ in range(N)]
exist = {}

for i in range(N):
    n = int(input().strip())
    numbers[i] = n
    try:
        exist[n] += 1
    except KeyError:
        exist[n] = 1

for i in range(N):
    result = 0
    j = 1
    while j * j <= numbers[i]:
        if numbers[i] % j == 0:
            result += exist.get(j, 0)
            
            if j != (r := numbers[i] // j):
                result += exist.get(r, 0)
        j += 1 
    print(result - 1)   # 자기 자신은 제외한다.