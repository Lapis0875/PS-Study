# Migrated from ./boj/boj1427.py by boj_validator
from sys import stdin

N: int = int(stdin.readline())
numbers: list[int] = []

while N > 0:
    numbers.append(N % 10)
    N //= 10

def merge(array: list[int], start: int, middle: int, end: int):
    temp: list[int] = []
    if end - start < 2:    # 말단의 경우
        if array[start] < array[end]:
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
            if array[l] < array[r]:
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

def mergeSort(array: list[int], start: int, end: int):
    if (start < end):
        middle: int = (start + end) // 2
        mergeSort(array, start, middle)
        mergeSort(array, middle + 1, end)
        merge(array, start, middle, end)
        
mergeSort(numbers, 0, len(numbers) - 1)

print(''.join(map(str, numbers)))