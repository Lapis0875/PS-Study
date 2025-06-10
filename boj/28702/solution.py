input = open(0).readline

text = [input().strip() for _ in range(3)]
answer = 0

# FizzBuzz의 가능한 출력을 생각해보면, Fizz/Buzz/FizzBuzz로만 구성된 연속되는 3개의 숫자는 존재하지 않는다.
# 무조건 3개의 입력 중 하나는 숫자이므로, 그 숫자를 찾아 답을 찾아내면 된다.
for i, t in enumerate(text):
    if t.isdigit():
        answer = int(t) + (3 - i) 

if answer > 0:
    if answer % 15 == 0:
        print("FizzBuzz")
    elif answer % 3 == 0:
        print("Fizz")
    elif answer % 5 == 0:
        print("Buzz")
    else:
        print(answer)
else:
    print(text[0])