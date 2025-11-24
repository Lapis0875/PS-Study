from math import sqrt
input = open(0).readline

def is_prime(n):
    if n < 2:
        return False
    
    for i in range(2, int(sqrt(n)) + 1):
        if n % i == 0:
            return False
    return True

for _ in range(int(input())):
    N = int(input())
    if N <= 2:
        print(2)
    else:
        if N % 2 == 0:
            N += 1
        while not is_prime(N):
            N += 2
        print(N)
