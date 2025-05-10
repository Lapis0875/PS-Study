from sys import stdin

def is_palindrome(x):
    for i in range(len(x) // 2):
        if x[i] != x[-(i + 1)]:
            return False
    return True

while True:
    x_list = list(map(int, stdin.readline().rstrip()))
    if len(x_list) == 1: # 종료 조건 (사실 0 제외하면 5자리 이상인데 그냥 자리수만 세도 맞지 않을까?)
        break
    
    if is_palindrome(x_list):
        print(0)
    else:
        result = 0
        while not is_palindrome(x_list):
            result += 1
            x_list[-1] += 1
            for i in range(len(x_list)-1, 0, -1):   # 자리 올림 처리
                if x_list[i] == 10:
                    x_list[i] = 0
                    x_list[i-1] += 1
        print(result)