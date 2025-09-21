input = open(0).readline
a, b, c = sorted(map(int, input().split()))
diff = a + b - c
if diff > 0: # a + b > c
    print(a + b + c)
else:
    # a <= b <= c 순으로 정렬되있을 때 a + b <= c인 경우, 
    # a + b > c로 바꾸기 위해서 c에서 (c - (a + b))만큼을 빼주면 a + b = c가 된다. 이때, c에서 임의의 작은 수를 빼 a + b > c로 만들면 되는데 막대의 길이는 모두 양의 정수이므로 임의의 작은 수는 1이다.
    # 따라서, c에서 c - (a + b) + 1 만큼을 빼준 값이 줄어든 c 막대의 길이가 되고, 이 상태에서 삼각형의 둘레는 a + b + c - c + a + b - 1이므로 2a + 2b - 1로 정리할 수 있다.
    print(2 * a + 2 * b - 1) # 막대기의 길이는 양의 정수.