from functools import cmp_to_key
from collections import deque
input = open(0).readline

N = int(input())
points = sorted((tuple(map(int, input().split())) for _ in range(N)), key=cmp_to_key(lambda p1, p2: p1[1] - p2[1] if p1[1] != p2[1] else p1[0] - p2[0]))

def ccw(p1, p2, p3):
    return (p1[0] * p2[1] + p2[0] * p3[1] + p3[0] * p1[1]) - (p1[1] * p2[0] + p2[1] * p3[0] + p3[1] * p1[0])

def dist(p1, p2):
    return (p1[0] - p2[0]) ** 2 + (p1[1] - p2[1]) ** 2

def cmp(p1, p2):
    c = ccw(points[0], p1, p2)
    if c == 0:
        return dist(points[0], p1) - dist(points[0], p2)
    return -c

points = sorted(points, key=cmp_to_key(cmp))

stack = deque([points[0], points[1]])
for i in range(2, N):
    while len(stack) >= 2:
        b = stack.pop()
        a = stack[-1]
        if ccw(points[i], a, b) > 0:
            stack.append(b)
            break
    stack.append(points[i])

print(len(stack))