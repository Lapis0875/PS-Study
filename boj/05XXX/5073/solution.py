input = open(0).readline
while True:
    a, b, c = sorted(map(int, input().split()))
    if a == 0 and b == 0 and c == 0:
        break

    if a + b <= c:
        print("Invalid")
    elif a == b:
        if b == c:
            print("Equilateral")
        else:
            print("Isosceles")
    elif b == c or a == c:
        print("Isosceles")
    else:
        print("Scalene")
