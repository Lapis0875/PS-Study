input = open(0).readline
N, M = map(int, input().split())
Customers = tuple(map(int, input().split()))
pottery = [False for _ in range(N)] # 손님 수 만큼 토기를 만들어야 한다. (재사용 불가) False는 토기가 만들어지지 않음, True면 만들어짐.
coffee = [False for _ in range(N)]   # 손님 수 만큼 커피를 담아야 한다. False는 커피가 담기지 않음, True면 담김.
pottery_made = 0        # 지금까지 만들어진 토기의 개수. 또한 새로 만들 토기가 저장될 인덱스와 같다.
coffee_to_serve = 0     # 손님에게 내보낼 가장 빠른 커피의 인덱스
customer_idx = 0        # 현재 커피를 받지 못한 손님들 중 가장 빠른 사람의 인덱스.

for t in range(Customers[-1] + 1):  # 마지막 손님이 커피를 받는 시간까지
    if customer_idx >= N:   # 모든 손님을 수용한 경우, 이미 결과를 알기 때문에 더이상 반복하지 않는다.
        print("success")
        break

    if t == Customers[coffee_to_serve]:    # 손님이 카페에 도착한 경우.
        if coffee[coffee_to_serve]:     # 커피가 준비되어 있는 경우.
            coffee_to_serve += 1
        else:   # 커피가 담긴 토기가 준비되지 않은 경우.
            print("fail")
            break
    elif t >= Customers[customer_idx] - M:  # 다음 손님을 대비해 토기를 만들어야 하는 경우.
        if pottery_made < N and not pottery[customer_idx]:
            pottery[pottery_made] = True
            pottery_made += 1
        else:
            coffee[customer_idx] = True
            customer_idx += 1
    elif pottery_made < N:   # 당장 급하게 해야 할 일이 없는 경우, 커피는 담지 않고 토기만 미리 준비한다.
        pottery[pottery_made] = True
        pottery_made += 1
else:
    print("success")