from sys import stdin
from typing import Final

N: Final[int] = int(stdin.readline())
Point = tuple[int, int]

def parsePoint(s: str) -> Point:
    """좌표를 나타내는 문자열 s를 좌표로 변환한다.

    Args:
        s (str): 좌표를 나타내는 문자열. "x y\n" 형태로 주어진다.

    Returns:
        Point: (x: int, y: int)로 좌표를 표현하는 튜플
    """
    x, y = s.split()
    return int(x), int(y)

points: list[Point] = [parsePoint(stdin.readline()) for _ in range(N)]

def comparePoint(a: Point, b: Point) -> bool:
    """2차원 좌표계의 두 점 a와 b를 문제의 조건에 따라 비교한다.

    Args:
        a (Point): 2차원 좌표계 상의 좌표
        b (Point): 2차원 좌표계 상의 좌표

    Returns:
        bool: a가 b보다 크다면 True, 그렇지 않다면 False.
    """
    x1, y1 = a
    x2, y2 = b
    if (x1 > x2):
        return True
    elif (x1 == x2 and y1 > y2):
        return True
    else:
        return False

def mergeSort(start: int, end: int):
    """입력으로 받은 좌표의 배열을 병합 정렬 알고리즘으로 정렬한다.

    Args:
        start (int): 병합 정렬의 시작 인덱스
        end (int): 병합 정렬의 끝 인덱스
    """
    if start < end:
        mid: int = (start + end) // 2
        
        # Divide
        mergeSort(start, mid)
        mergeSort(mid + 1, end)
        
        temp: list[Point] = []
        
        # Merge
        if (end - start) < 2:
            if comparePoint(points[start], points[end]):
                temp.append(points[end])
                temp.append(points[start])
            else:
                temp.append(points[start])
                temp.append(points[end])
        else:
            left: int = start
            right: int = mid + 1
            
            while left <= mid and right <= end:
                if comparePoint(points[right], points[left]):   # points[right]가 더 클 때
                    temp.append(points[left])
                    left += 1
                else:
                    temp.append(points[right])
                    right += 1
            while left <= mid:
                temp.append(points[left])
                left += 1
            while right <= end:
                temp.append(points[right])
                right += 1
            
        for i, point in zip(range(start, end + 1), temp):
            points[i] = point
            
mergeSort(0, N - 1)    

for point in points:
    print(*point)
