from collections import deque
input = open(0).readline

def D(number):
    return (number * 2) % 10000

def S(number):
    return (number + 9999) % 10000

def L(number):
    return number // 1000 + number % 1000 * 10

def R(number):
    return number // 10 + number % 10 * 1000

for _ in range(int(input())):   # 각각의 테스트 케이스에 대해 연산 수행
    A, B = map(int, input().split())

    # BFS
    queue = deque([A])
    prev = [0] * 10000
    prev[A] = A
    while queue:
        cur_number = queue.popleft()
        for cmd in (D, S, L, R):
            next_number = cmd(cur_number)
            if prev[next_number] == 0:    # 같은 숫자로 다시 돌아오는 경우는 사이클이 형성된 것. 이후의 탐색이 효율적인 경로가 아님이 자명함.
                prev[next_number] = (cur_number, cmd.__name__)
                if next_number == B:    # 정답을 찾았다면 즉시 종료.
                    break
                queue.append(next_number)
    
    # 경로 출력
    stack = []
    while B != A:
        B, cmd = prev[B]
        stack.append(cmd)
    print("".join(stack[::-1]))
