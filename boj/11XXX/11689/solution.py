from math import sqrt
input = open(0).readline
N = int(input())

count = N
for i in range(2, int(sqrt(N)) + 1):
    if N % i == 0:
        count -= count // i     # 오일러 피 함수 계산
        
        while N % i == 0: # 전체 합성수에서 이번에 계산한 소인수를 완전히 제거한다.
            N //= i

if N > 1: # 아직 소인수가 남아있는 경우
    count -= count // N

print(count)