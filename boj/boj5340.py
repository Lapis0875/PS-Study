from sys import stdin, stdout
from typing import cast, Final

T: Final[int] = int(stdin.readline())

def task():
    P: Final[str] = stdin.readline()[:-1]
    N: Final[int] = int(stdin.readline())
    x: list[int] = cast(list[int], eval(stdin.readline()[:-1]))
    
    length: int = N
    removal: int = 0        # 지울 인덱스를 가리킨다.
    for func in P:
        if func == "R":
            removal = -1 if removal == 0 else 0     # 배열을 앞에서 혹은 뒤에서 처리한다.
        else:
            if length == 0:
                stdout.write("error\n")
                return
            x.pop(removal)
            length -= 1
    
    stdout.write("[")
    if length == 0:
        stdout.write("]\n")
    elif removal == -1:
        for i in x[length-1:0:-1]:  # length-1 ~ 1까지 역방향 반복 후
            stdout.write(f"{i},")
        stdout.write(f"{x[0]}]\n")  # 첫 원소를 별도로 처리한다.
    else:
        for i in x[:length-1]:      # 0 ~ length-2까지 정방향 반복 후
            stdout.write(f"{i},")
        stdout.write(f"{x[-1]}]\n") # 마지막 원소를 별도로 처리한다.

for _ in range(T):
    task()
