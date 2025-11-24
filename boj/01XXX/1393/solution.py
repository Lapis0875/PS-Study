from math import gcd
input = open(0).readline
x_s, y_s = tuple(map(int, input().split()))     # 정류장 위치
x_e, y_e, dx, dy = map(int, input().split())    # 현재 위치 x_e, y_e, 초당 x/y축 변화량 dx, dy

# 정류장과 반대 방향으로 이동할 때 예외처리
neg_x = False
neg_y = False
if (dy < 0 and y_s - y_e > 0) or (dy > 0 and y_s - y_e < 0) or (dx < 0 and x_s - x_e > 0) or (dx > 0 and x_s - x_e < 0):
    print(x_e, y_e)

# dx나 dy가 0일 때 예외처리
elif dx == 0:
    if dy == 0:
        print(x_e, y_e)
    else:
        print(x_e, y_s)
elif dy == 0:
    print(x_s, y_e)
else:
    # 1. 기준 직선 (철도)
    # 기울기 (dy/dx)이고 (x_e, y_e)를 지나는 직선
    # dy/dx = (y - y_e) / (x - x_e)
    # dy(x - x_e) = dx(y - y_e)
    # dy * x - dx * y = dy * x_e - dx* y_e

    # 2. 수직이 되는 직선 (정거장)
    # 기울기 (-dx/dy)이고 (x_s, y_s)를 지나는 직선
    # -dx/dy = (y - y_s) / (x - x_s)
    # -dx * x + dx * x_s = dy * y - dy * y_s
    # -dx * x - dy * y = -dx * x_s - dy * y_s
    # dx * x + dy * y = dx * x_s + dy * y_s

    # 3. 연립방정식의 해 구하기 (두 직선의 교점)
    # dy * x - dx * y = dy * x_e - dx * y_e (1)
    # dx * x + dy * y = dx * x_s + dy * y_s (2)

    # (1)에 dx, 2에 dy를 곱한 후 서로 빼 x를 제한다.
    # (dx * dy) * x - dx^2 * y = (dx * dy) * x_e - dx^2 * y_e (1)
    # (dx * dy) * x + dy^2 * y = (dx * dy) * x_s + dy^2 * y_s (2)

    # (2)에서 (1)을 뺀 뒤 식을 y에 대해 정리한다.
    # (dy^2 + dx^2) * y = (dx * dy) (x_s - x_e) + dy^2 * y_s + dx^2 * y_e
    y = ((dx * dy) * (x_s - x_e) + dy * dy * y_s + dx * dx * y_e) // (dy * dy + dx * dx) # 항상 정수 답이 나오는 입력만 주어짐

    # (1)을 이용해 y에 대한 x를 찾는다.
    # dy * x = dx * (y - y_e) + dy * x_e
    x = dx * (y - y_e) // dy + x_e
    print(x, y)