input = open(0).readline
# daldidalgo를 한번 쓰는데 걸리는 시간 : 8 (d/a/l/d/i/dal/g/o)
# daldidan을 마지막에 쓰는데 걸리는 시간 : 2 (daldida/n)
# daldidalgo를 N번 쓰는데 걸리는 시간은 log2(N) + 10 꼴이 된다.
# N이 짝수라면, daldidalgo를 복사할 때 마다 2의 거듭제곱 꼴로 그 크기가 커지므로 로그 횟수에 N번 반복한 크기를 만들 수 있다. 이후에 daldidan을 한번 더 써주면 된다.
# N이 홀수라면, N // 2 + 1 까지 만들고, 앞서 만든 문자에서 ~~daldida 까지 복사한 뒤 n만 써주면 된다. daldidan을 만드는데 1초만 걸리지만, 복사하는 횟수가 1 더 많으므로 결과는 같다.
N = int(input())
# N을 2진수로 표현 -> 비트가 1인 모든 자리에 대해: 해당 자리만큼 daldidalgo를 반복하는데 필요한 시간을 계산 (단, 한번 계산된 전체 부분은 이후에 재사용 가능)
time = 0 # daldidalgo 1번 썼음
while N > 1:
    N >>= 1
    time += 1
print(time + 10)