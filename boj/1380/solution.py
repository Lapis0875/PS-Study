from sys import stdin

girls: list[str] = ["" for _ in range(101)]     # 인덱스를 1부터 사용하기 위해 0번에 더미 데이터 포함.
check: list[bool] = [False for _ in range(101)]

scene: int = 1
while (n := stdin.readline()[:-1]) != "0":
    N: int = int(n)
    for i in range(1, N + 1):
        girls[i] = stdin.readline()[:-1]        # 학생 정보를 인덱스에 저장한다.
    for _ in range(2 * N - 1):
        idx, _ = stdin.readline()[:-1].split()  # A, B는 문제 풀이에 전혀 상관없는 정보이므로 버린다.
        check[int(idx)] = not check[int(idx)]   # 귀걸이 압수 여부를 토글한다. 반복 종료 이후 유일하게 True인 학생의 인덱스를 찾는다.
    remain: int = check.index(True)
    print(scene, girls[remain])
    check[remain] = False                       # 재사용을 위해 다시 False로 만든다.
    scene += 1
