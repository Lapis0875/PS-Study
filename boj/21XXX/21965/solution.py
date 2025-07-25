input = open(0).readline
N = int(input())
A = list(map(int, input().split()))

result = True       # 결과값을 나타내는 변수
idx = 0             # idx는 감소하기 직전의 인덱스, 즉 순열 내에서 가장 큰 값의 인덱스가 된다.
idx_lock = False    # 한 번 감소하기 시작한 뒤로는 다시 증가해선 안된다.
for i in range(1, N):
    if A[i] == A[i - 1] or (idx_lock and i > idx and A[i] > A[i - 1]):  # 중복된 수가 존재하거나, 감소한 뒤로 다시 증가하는 경우
        result = False
        break
    
    if not idx_lock:            # 최초 감소하는 지점을 찾기 위한 조건문.
        if A[i] > A[i-1]:
            idx = i
        elif A[i] < A[i-1]:
            idx_lock = True
        
print("YES" if result else "NO")