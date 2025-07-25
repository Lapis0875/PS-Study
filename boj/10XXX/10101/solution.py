input = open(0).readline
degrees = [int(input()) for _ in range(3)]

if sum(degrees) == 180:
    if degrees[0] == degrees[1]:
        if degrees[1] == degrees[2]: # 세 각이 같으면 셋 다 60도일 것이다.
            print("Equilateral")
        else: # 두 각이 같은 경우
            print("Isosceles")
    elif degrees[1] == degrees[2] or degrees[0] == degrees[2]:   # 두 각이 같은 경우
        print("Isosceles")
    else:
        print("Scalene")
else:
    print("Error")