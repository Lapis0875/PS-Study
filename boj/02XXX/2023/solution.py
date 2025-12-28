from math import sqrt
input = open(0).readline
N = int(input())

def is_prime(number):
    if number < 10:
        return number == 2 or number == 3 or number == 5 or number == 7 

    for i in range(2, int(sqrt(number)) + 1):
        if number % i == 0:
            return False
    return True

def build(number, index):
    if index == N:
        print(number)
        return
    
    for d in range(10):
        new_number = number * 10 + d
        if is_prime(new_number):
            build(new_number, index + 1)

# 왼쪽에서 첫 자리의 숫자는 무조건 한 자리 소수여야 한다.
for i in (2, 3, 5, 7):
    build(i, 1)
