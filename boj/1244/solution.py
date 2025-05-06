from sys import stdin

SW_CNT = int(stdin.readline())                              # 스위치 개수
SW_LIST = [-1, ]                                            # 초기 스위치 정보 (인덱스 1부터 시작하게 하려고 0번에 False 넣어둠.)
SW_LIST.extend(map(int, stdin.readline().split()))          # 1번부터 N번까지 스위치 정보 받음.
STU_CNT = int(stdin.readline())                             # 학생 수


def turn_switch(x):
    """
    x번 스위치의 상태를 바꾼다.

    Args:
        x (int): 바꾸려는 스위치의 번호. (1~N으로 인덱스 사용.)
    """
    SW_LIST[x] = 1 - SW_LIST[x]


def boy(x: int):
    """
    남학생의 스위치 조작 방식을 구현한다.

    Args:
        x (int): 남학생이 받은 숫자.
    """
    for i in range(x, SW_CNT+1, x):
        turn_switch(i)

def girl(x: int):
    """
    여학생의 스위치 조작 방식을 구현한다.

    Args:
        x (int): 여학생이 받은 숫자.
    """
    turn_switch(x)   # 중앙 먼저 스위치 바꾸기
    # 좌/우 경계 설정
    gap = 1
    while x - gap >= 1 and x + gap <= SW_CNT and SW_LIST[x-gap] == SW_LIST[x+gap]:
        turn_switch(x - gap)
        turn_switch(x + gap)
        gap += 1

for _ in range(STU_CNT):
    gender, x = map(int, stdin.readline().split())
    if gender == 1:
        boy(x)
    else:
        girl(x)

i = 1
while i <= SW_CNT:
    print(" ".join(map(str, SW_LIST[i: i+20])))
    i += 20
