from sys import stdin

N: int = int(stdin.readline())
arr: list[str] = list(set(stdin.readline().rstrip() for _ in range(N)))
N = len(arr)

def compare(a: str, b: str) -> bool:
    """두 문자열을 문제의 조건에 맞게 비교해, a가 b보다 작을 때 True를 반환한다."""
    lenA: int = len(a)
    lenB: int = len(b)
    
    if lenA == lenB:
        for charA, charB in zip(a, b):
            if charA < charB:
                return True
            elif charA > charB:
                return False
    else:
        return lenA < lenB
    return False

def merge(array: list[str], start: int, middle: int, end: int):
    temp: list[str] = []
    if end - start < 2:    # 말단의 경우
        if compare(array[start], array[end]):     # 왼쪽 요소가 오른쪽 요소보다 작다.
            temp.append(array[start])
            temp.append(array[end])
        else:
            temp.append(array[end])
            temp.append(array[start])
    else:
        l: int = start
        r: int = middle + 1
        # 두 부분 리스트를 병합한다.
        while l <= middle and r <= end:
            if compare(array[l], array[r]):     # 왼쪽 요소가 오른쪽 요소보다 작다.
                temp.append(array[l])
                l += 1
            else:
                temp.append(array[r])
                r += 1
        # 남아있는 부분 리스트를 모두 임시 리스트에 병합한다.
        while l <= middle:
            temp.append(array[l])
            l += 1
        while r <= end:
            temp.append(array[r])
            r += 1
    for i, e in zip(range(start, end + 1), temp):    # start부터 end까지의 인덱스 i와, temp 리스트의 각 요소 e로 반복한다.
        array[i] = e

def mergeSort(array: list[str], start: int, end: int):
    if (start < end):
        middle: int = (start + end) // 2
        mergeSort(array, start, middle)
        mergeSort(array, middle + 1, end)
        merge(array, start, middle, end)

mergeSort(arr, 0, N - 1)

for word in arr:
    print(word)