from sys import stdin

N, K = map(int, stdin.readline().split())
coins: list[int] = [int(stdin.readline()) for _ in range(N)]    # 이미 오름차순 정렬된 입력이다.

count: int = 0
while K > 0:
    for coin_value in coins[::-1]:
        if K >= coin_value:
            count += K // coin_value
            K %= coin_value

print(count)