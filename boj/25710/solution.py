from sys import stdin

N = int(stdin.readline())
numbers = [0 for _ in range(1001)]  # 1~999까지의 수만 입력값 내에 존재하므로, 그 개 수를 세자.
calc_array = []

for number in map(int, stdin.readline().split()):
    numbers[number] += 1
    if numbers[number] <= 2:
        calc_array.append(number)   # 어짜피 2개 이상으로 중복되어도 2개만 포함된거랑 경우의 수는 같다 (자기 자신과의 곱, 자기 자신과 다른 수와의 곱)

res = 0
for i in range(0, len(calc_array)):
    for j in range(i+1, len(calc_array)):
        x = calc_array[i] * calc_array[j]
        r = 0
        while x > 0:
            r += x % 10
            x //= 10
        if r > res:
            res = r
print(res)
