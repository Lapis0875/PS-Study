# Migrated from ./boj/boj11651.py by boj_validator
from sys import stdin

Point = tuple[int, int]
N: int = int(stdin.readline())

points: list[Point] = [tuple(map(int, stdin.readline().split())) for _ in range(N)]

def comparePoint(a: Point, b: Point) -> bool:
    ax, ay = a
    bx, by = b
    if ay < by:
        return False
    elif ay == by and ax < bx:
        return False
    return True

def merge(array: list[Point], start: int, middle: int, end: int):
    temp: list[Point] = []
    if end - start < 2:    # 말단의 경우
        if comparePoint(array[start], array[end]):
            temp.append(array[end])
            temp.append(array[start])
        else:
            temp.append(array[start])
            temp.append(array[end])
    else:
        l: int = start
        r: int = middle + 1
        # 두 부분 리스트를 병합한다.
        while l <= middle and r <= end:
            if comparePoint(array[l], array[r]):
                temp.append(array[r])
                r += 1
            else:
                temp.append(array[l])
                l += 1
        # 남아있는 부분 리스트를 모두 임시 리스트에 병합한다.
        while l <= middle:
            temp.append(array[l])
            l += 1
        while r <= end:
            temp.append(array[r])
            r += 1
    for i, e in zip(range(start, end + 1), temp):    # start부터 end까지의 인덱스 i와, temp 리스트의 각 요소 e로 반복한다.
        array[i] = e

def mergeSort(array: list[Point], start: int, end: int):
    if (start < end):
        middle: int = (start + end) // 2
        mergeSort(array, start, middle)
        mergeSort(array, middle + 1, end)
        merge(array, start, middle, end)
        
mergeSort(points, 0, N - 1)

for p in points:
    print(*p)